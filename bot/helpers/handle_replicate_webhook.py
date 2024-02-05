import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey

from bot.database.models.common import Model, Currency, Quota
from bot.database.models.generation import Generation, GenerationStatus
from bot.database.models.request import Request, RequestStatus
from bot.database.models.transaction import TransactionType, ServiceType
from bot.database.models.user import User, UserSettings
from bot.database.operations.face_swap_package import update_used_face_swap_package, get_used_face_swap_package
from bot.database.operations.generation import get_generation, update_generation, get_generations_by_request_id
from bot.database.operations.request import get_request, update_request
from bot.database.operations.transaction import write_transaction
from bot.database.operations.user import get_user, update_user
from bot.handlers.face_swap_handler import PRICE_FACE_SWAP, handle_face_swap
from bot.handlers.music_gen_handler import PRICE_MUSIC_GEN, handle_music_gen
from bot.helpers.send_audio import send_audio
from bot.helpers.send_images import send_image
from bot.keyboards.common import build_reaction_keyboard


async def handle_replicate_webhook(bot: Bot, dp: Dispatcher, prediction: dict):
    generation = await get_generation(prediction.get("id"))
    if not generation:
        return False
    elif generation.status == GenerationStatus.FINISHED:
        return True

    generation_error, generation_result = prediction.get("error", False), prediction.get("output", {})
    seconds = prediction.get("metrics", {}).get("predict_time")
    if generation_error or not generation_result:
        generation.has_error = True
        await update_generation(generation.id, {
            "status": GenerationStatus.FINISHED,
            "has_error": generation.has_error,
            "seconds": seconds,
        })
        logging.error(f"Error in replicate_webhook: {prediction.get('logs')}")
    else:
        generation.status = GenerationStatus.FINISHED
        if generation.model == Model.FACE_SWAP:
            generation.result = generation_result.get("image")
        else:
            generation.result = generation_result
        generation.seconds = seconds
        await update_generation(generation.id, {
            "status": generation.status,
            "result": generation.result,
            "seconds": generation.seconds,
        })

    request = await get_request(generation.request_id)
    user = await get_user(request.user_id)

    if request.model == Model.FACE_SWAP:
        await handle_replicate_face_swap(bot, dp, user, request, generation)
    elif request.model == Model.MUSIC_GEN:
        await handle_replicate_music_gen(bot, dp, user, request, generation)

    return True


async def handle_replicate_face_swap(bot: Bot,
                                     dp: Dispatcher,
                                     user: User,
                                     request: Request,
                                     generation: Generation):
    reply_markup = build_reaction_keyboard(generation.id)
    await send_image(bot, user.telegram_chat_id, generation.result, reply_markup)

    current_count = await dp.storage.redis.incr(request.id)
    if current_count == request.requested and request.status != RequestStatus.FINISHED:
        request.status = RequestStatus.FINISHED
        await update_request(request.id, {
            "status": request.status
        })

        request_generations = await get_generations_by_request_id(request.id)
        success_generations = []
        used_face_swap_package_used_images = []
        total_seconds = 0
        for request_generation in request_generations:
            if request_generation.result:
                success_generations.append(request_generation.result)
            if request_generation.details.get('used_face_swap_package_used_image'):
                used_face_swap_package_used_images.append(
                    request_generation.details.get('used_face_swap_package_used_image')
                )
            total_seconds += request_generation.seconds

        total_result = len(success_generations)

        used_face_swap_package = await get_used_face_swap_package(
            generation.details.get("used_face_swap_package_id")
        )
        if request.details.get("is_test"):
            update_tasks = [
                write_transaction(
                    user_id=user.id,
                    type=TransactionType.EXPENSE,
                    service=ServiceType.FACE_SWAP,
                    amount=round(PRICE_FACE_SWAP * total_seconds, 6),
                    currency=Currency.USD,
                    quantity=total_result,
                    details={
                        'name': request.details.get("face_swap_package_name"),
                        'images': success_generations,
                        'seconds': total_seconds,
                    }),
            ]
        else:
            quantity_to_delete = total_result
            quantity_deleted = 0
            while quantity_deleted != quantity_to_delete:
                if user.monthly_limits[Quota.FACE_SWAP] != 0:
                    user.monthly_limits[Quota.FACE_SWAP] -= 1
                    quantity_deleted += 1
                elif user.additional_usage_quota[Quota.FACE_SWAP] != 0:
                    user.additional_usage_quota[Quota.FACE_SWAP] -= 1
                    quantity_deleted += 1
                else:
                    break

            update_tasks = [
                write_transaction(
                    user_id=user.id,
                    type=TransactionType.EXPENSE,
                    service=ServiceType.FACE_SWAP,
                    amount=round(PRICE_FACE_SWAP * total_seconds, 6),
                    currency=Currency.USD,
                    quantity=quantity_to_delete,
                    details={
                        'name': request.details.get("face_swap_package_name", "CUSTOM"),
                        'images': success_generations,
                        'seconds': total_seconds,
                    }
                ),
                update_user(user.id, {
                    "monthly_limits": user.monthly_limits,
                    "additional_usage_quota": user.additional_usage_quota
                }),
            ]
            if used_face_swap_package and used_face_swap_package_used_images:
                update_tasks.append(
                    update_used_face_swap_package(used_face_swap_package.id, {
                        "used_images": used_face_swap_package.used_images + used_face_swap_package_used_images,
                    })
                )

        await asyncio.gather(*update_tasks)

        state = FSMContext(
            storage=dp.storage,
            key=StorageKey(
                chat_id=int(user.telegram_chat_id),
                user_id=int(user.id),
                bot_id=bot.id,
            )
        )
        await state.clear()
        await handle_face_swap(bot, user.telegram_chat_id, state, user.id)

        await bot.delete_message(user.telegram_chat_id, request.message_id)


async def handle_replicate_music_gen(bot: Bot,
                                     dp: Dispatcher,
                                     user: User,
                                     request: Request,
                                     generation: Generation):
    prompt = generation.details.get('prompt')
    duration = int(generation.details.get('duration'))

    reply_markup = build_reaction_keyboard(generation.id)
    caption = f"🎵 {(user.monthly_limits[Quota.MUSIC_GEN] + user.additional_usage_quota[Quota.MUSIC_GEN]) - duration}" \
        if user.settings[Model.MUSIC_GEN][UserSettings.SHOW_USAGE_QUOTA] \
        else "🎵"
    await send_audio(
        bot,
        user.telegram_chat_id,
        generation.result,
        caption,
        prompt,
        duration,
        reply_markup,
    )

    if request.status != RequestStatus.FINISHED:
        request.status = RequestStatus.FINISHED
        await update_request(request.id, {
            "status": request.status
        })

        quantity_to_delete = duration
        quantity_deleted = 0
        while quantity_deleted != quantity_to_delete:
            if user.monthly_limits[Quota.MUSIC_GEN] != 0:
                user.monthly_limits[Quota.MUSIC_GEN] -= 1
                quantity_deleted += 1
            elif user.additional_usage_quota[Quota.MUSIC_GEN] != 0:
                user.additional_usage_quota[Quota.MUSIC_GEN] -= 1
                quantity_deleted += 1
            else:
                break

        update_tasks = [
            write_transaction(
                user_id=user.id,
                type=TransactionType.EXPENSE,
                service=ServiceType.MUSIC_GEN,
                amount=round(PRICE_MUSIC_GEN * generation.seconds, 6),
                currency=Currency.USD,
                quantity=quantity_to_delete,
                details={
                    'result': generation.result,
                    'prompt': prompt,
                    'duration': duration,
                },
            ),
            update_user(user.id, {
                "monthly_limits": user.monthly_limits,
                "additional_usage_quota": user.additional_usage_quota
            }),
        ]

        await asyncio.gather(*update_tasks)

        state = FSMContext(
            storage=dp.storage,
            key=StorageKey(
                chat_id=int(user.telegram_chat_id),
                user_id=int(user.id),
                bot_id=bot.id,
            )
        )
        await state.clear()

        await handle_music_gen(bot, user.telegram_chat_id, state, user.id)

        await bot.delete_message(user.telegram_chat_id, request.message_id)
