from datetime import datetime, timezone

from bot.database.models.common import (
    Currency,
    Model,
    Quota,
    GPTVersion,
    DALLEResolution,
    DALLEQuality,
    DALLEVersion,
    MidjourneyVersion,
    SunoSendType,
)
from bot.database.models.subscription import SubscriptionType, SubscriptionLimit


class UserSettings:
    SHOW_THE_NAME_OF_THE_CHATS = 'show_the_name_of_the_chats'
    SHOW_THE_NAME_OF_THE_ROLES = 'show_the_name_of_the_roles'
    SHOW_USAGE_QUOTA = 'show_usage_quota'
    TURN_ON_VOICE_MESSAGES = 'turn_on_voice_messages'
    VOICE = 'voice'
    RESOLUTION = 'resolution'
    QUALITY = 'quality'
    VERSION = 'version'
    SEND_TYPE = 'send_type'


class UserGender:
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    UNSPECIFIED = 'UNSPECIFIED'


class User:
    COLLECTION_NAME = "users"

    id: str
    first_name: str
    last_name: str
    username: str
    current_chat_id: str
    telegram_chat_id: str
    language_code: str
    gender: UserGender
    is_premium: bool
    is_blocked: bool
    current_model: Model
    currency: Currency
    balance: float
    subscription_type: SubscriptionType
    last_subscription_limit_update: datetime
    monthly_limits: dict
    additional_usage_quota: dict
    settings: dict
    referred_by: str
    discount: int
    created_at: datetime
    edited_at: datetime

    DEFAULT_ADDITIONAL_USAGE_QUOTA = {
        Quota.CHAT_GPT3: 0,
        Quota.CHAT_GPT4: 0,
        Quota.ADDITIONAL_CHATS: 0,
        Quota.DALL_E: 0,
        Quota.MIDJOURNEY: 0,
        Quota.FACE_SWAP: 0,
        Quota.MUSIC_GEN: 0,
        Quota.SUNO: 0,
        Quota.FAST_MESSAGES: False,
        Quota.VOICE_MESSAGES: False,
        Quota.ACCESS_TO_CATALOG: False,
    }

    DEFAULT_SETTINGS = {
        Model.CHAT_GPT: {
            UserSettings.SHOW_THE_NAME_OF_THE_CHATS: False,
            UserSettings.SHOW_THE_NAME_OF_THE_ROLES: False,
            UserSettings.SHOW_USAGE_QUOTA: True,
            UserSettings.TURN_ON_VOICE_MESSAGES: False,
            UserSettings.VOICE: 'alloy',
            UserSettings.VERSION: GPTVersion.V3,
        },
        Model.DALL_E: {
            UserSettings.SHOW_USAGE_QUOTA: True,
            UserSettings.RESOLUTION: DALLEResolution.LOW,
            UserSettings.QUALITY: DALLEQuality.STANDARD,
            UserSettings.VERSION: DALLEVersion.V3,
        },
        Model.MIDJOURNEY: {
            UserSettings.SHOW_USAGE_QUOTA: True,
            UserSettings.VERSION: MidjourneyVersion.V6,
        },
        Model.FACE_SWAP: {
            UserSettings.SHOW_USAGE_QUOTA: True,
        },
        Model.MUSIC_GEN: {
            UserSettings.SHOW_USAGE_QUOTA: True,
        },
        Model.SUNO: {
            UserSettings.SHOW_USAGE_QUOTA: True,
            UserSettings.SEND_TYPE: SunoSendType.VIDEO,
        },
    }

    def __init__(
        self,
        id: str,
        first_name: str,
        last_name: str,
        username: str,
        current_chat_id: str,
        telegram_chat_id: str,
        gender=UserGender.UNSPECIFIED,
        language_code="en",
        is_premium=False,
        is_blocked=False,
        current_model=Model.CHAT_GPT,
        currency=Currency.RUB,
        balance=0,
        subscription_type=SubscriptionType.FREE,
        last_subscription_limit_update=None,
        monthly_limits=None,
        additional_usage_quota=None,
        settings=None,
        referred_by=None,
        discount=0,
        created_at=None,
        edited_at=None,
    ):
        self.id = str(id)
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.gender = gender
        self.language_code = language_code
        self.is_premium = is_premium
        self.is_blocked = is_blocked
        self.current_model = current_model
        self.currency = currency
        self.balance = balance
        self.subscription_type = subscription_type
        self.current_chat_id = str(current_chat_id)
        self.telegram_chat_id = str(telegram_chat_id)
        self.monthly_limits = monthly_limits if monthly_limits is not None \
            else SubscriptionLimit
        self.additional_usage_quota = additional_usage_quota if additional_usage_quota is not None \
            else self.DEFAULT_ADDITIONAL_USAGE_QUOTA
        self.settings = settings if settings is not None else self.DEFAULT_SETTINGS
        self.referred_by = referred_by
        self.discount = discount

        current_time = datetime.now(timezone.utc)
        self.last_subscription_limit_update = last_subscription_limit_update \
            if last_subscription_limit_update is not None else current_time
        self.created_at = created_at if created_at is not None else current_time
        self.edited_at = edited_at if edited_at is not None else current_time

    def to_dict(self):
        return vars(self)
