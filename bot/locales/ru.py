import random

from bot.locales.texts import Texts
from bot.database.models.common import Currency, Quota
from bot.database.models.package import PackageType
from bot.database.models.subscription import Subscription, SubscriptionType, SubscriptionPeriod, SubscriptionLimit
from bot.database.models.user import User, UserGender


class Russian(Texts):
    START = """
🤖 Добро пожаловать в будущее ИИ с GPTsTurboBot 🎉

Бот предоставляет доступ к искусственному интеллекту и нейросетям.
Отправьтесь в путешествие по миру ИИ с:
✉️ Неограниченным количеством запросов к ChatGPT 3... Ну, почти! Посмотрите наш тариф 'Бесплатно'
🧠 Мудростью ChatGPT 4, если сегодня вы чувствуете себя особенно умным
🎨 Художественными творениями с DALL-E 3, которые заставят Пикассо взглянуть дважды
😜 А хотели ли вы когда-нибудь поменяться лицами с Моной Лизой? Просто попросите нашу функцию Face Swap

Вот краткое руководство, чтобы начать:
✉️ Чтобы получить текстовый ответ, просто введите ваш запрос в чат
🌅 Чтобы создать изображение, сначала выберите модель ИИ в /mode, а затем дайте волю своему воображению!
🔄 Переключайтесь между разными нейросетями с помощью /mode в зависимости от ваших творческих потребностей
🔍 Используйте /mode, чтобы узнать больше о возможностях каждой модели ИИ
👁️‍🗨️ Погрузитесь в /catalog, чтобы выбрать специализированного помощника для ваших задач
📊 Проверьте информацию об использовании и подробности подписки в /profile
🔧 Дополнительно настройте свой опыт в /settings

И это ещё не всё! Просто нажмите /help, чтобы увидеть все волшебные команды ИИ, доступные вам.
Пусть ИИ станет вашим со-пилотом в этом приключении! 🚀
"""
    COMMANDS = """
🤖 Вот что вы можете исследовать:

👋 /start - <b>Обо мне</b>
🌍 /language - Переключайтесь на любой язык, <b>устанавливайте системные сообщения</b>.
🧠 /mode - <b>Переключайте модели нейросетей</b> на лету — <b>ChatGPT3</b>, <b>ChatGPT4</b>, <b>DALL-E 3</b> или <b>Face Swap</b>!
👤 /profile - <b>Посмотреть свой профиль</b>, чтобы узнать ваш квоту использования и многое другое.
🔧 /settings - <b>Настройте свой опыт</b> для бесшовного пользовательского опыта.
🎭 /catalog - <b>Выберите специализированного помощника</b> для задач, разработанных специально для вас.
💬 /chats - <b>Создайте, переключайтесь или удаляйте тематические чаты</b>.
💳 /subscribe или /buy - <b>Узнайте о наших подписках и преимуществах</b> или выберите индивидуальные пакеты.
🎁 /promo_code - <b>Раскройте эксклюзивные функции ИИ</b> и специальные предложения с вашим <b>промокодом</b>.
📡 /feedback - Оставьте обратную связь и <b>улучшите меня</b>.

Просто напишите или используйте команду, чтобы начать своё путешествие в мир ИИ! 🌟
"""
    FEEDBACK = """
🌟 <b>Ваше мнение важно!</b> 🌟

Привет! Мы всегда стремимся к улучшению, и ваша обратная связь для нас как золото. 💬✨

- Что-то вам особенно нравится в нашем боте? Расскажите нам!
- Есть предложения по функциям? Мы внимательно выслушаем!
- Что-то вас беспокоит? Мы здесь, чтобы устранить эти проблемы. 🐞
Просто напишите свои мысли и нажмите отправить. Всё так просто! Ваши идеи помогают нам расти и становиться лучше каждый день.
И помните, каждое ваше замечание — это шаг к тому, чтобы наш бот стал ещё круче. С нетерпением ждём от вас новостей! 💌
"""
    FEEDBACK_SUCCESS = """
🌟 <b>Обратная связь получена!</b> 🌟

Спасибо, что поделились своими мыслями! 💌
Ваше мнение - это секретный ингредиент нашего успеха. Мы готовим улучшения, и ваша обратная связь - ключевой элемент. 🍳🔑

Следите за обновлениями и новыми функциями, все они вдохновлены вами. А пока приятного общения! 🚀

Ваше мнение очень важно для нас! 💖
"""

    # Profile
    TELL_ME_YOUR_GENDER = "Скажите ваш пол:"
    YOUR_GENDER = "Ваш пол:"
    UNSPECIFIED = "Не указан 🤷"
    MALE = "Мужской 🚹"
    FEMALE = "Женский 🚺"
    SEND_ME_YOUR_PICTURE = """
📸 <b>Готовы к фототрансформации? Вот как начать!</b>

👍 <b>Рекомендации для идеального фото:</b>
- Чёткое селфи хорошего качества.
- На селфи должен быть только один человек.

👎 <b>Пожалуйста, избегайте таких фотографий:</b>
- Групповые фото.
- Животные.
- Дети до 18 лет.
- Фотографии в полный рост.
- Непристойные или обнажённые фотографии.
- Солнцезащитные очки или любые предметы, закрывающие лицо.
- Размытые или не в фокусе изображения.
- Видео и анимации.
- Сжатые или изменённые изображения.

Как только вы найдёте идеальный кадр, <b>загрузите свою фотографию</b> и дайте волшебству начаться 🌟
    """
    CHANGE_PHOTO = "Поменять фотографию 📷"
    CHANGE_PHOTO_SUCCESS = "📸 Фото успешно загружено! 🌟"
    CHANGE_GENDER = "Поменять пол 🚹🚺"

    # Language
    LANGUAGE = "Язык:"
    CHOOSE_LANGUAGE = "Выбранный язык: Русский 🇷🇺"

    # Promo code
    PROMO_CODE_INFO = """
🔓 <b>Откройте мир чудес ИИ с вашим секретным кодом!</b> 🌟

Если у вас есть промокод, просто введите его, чтобы раскрыть скрытые функции и особые сюрпризы. 🎁

Нет кода? Не беда! Просто нажмите 'Отменить', чтобы продолжить изучение вселенной ИИ без него. 🚀
"""
    PROMO_CODE_SUCCESS = """
🎉 <b>Ура! Вы нашли золотую жилу!</b> 🌟

Ваш промокод успешно активирован! Приготовьтесь окунуться в мир чудес ИИ с вашими новыми преимуществами. 🚀

Спасибо, что присоединились к нам в этом приключении на основе ИИ. Наслаждайтесь дополнительными возможностями и создавайте волшебство вместе с нами! ✨

Приятного исследования! 🤖🌐
"""
    PROMO_CODE_ALREADY_HAVE_SUBSCRIPTION = """
🚫 <b>Упс</b>

Кажется, ты уже в нашем эксклюзивном клубе подписчиков! 🌟
"""
    PROMO_CODE_EXPIRED_ERROR = """
🕒 <b>Ой, срок действия этого промокода истёк!</b>

Похоже, что этот промокод устарел. 📆 Это как сказка о Золушке, но без стеклянного башмачка. 🥿

Но не расстраивайтесь! Вы всё ещё можете изучать наши другие волшебные предложения с помощью /subscribe или /buy. В нашем мире ИИ всегда есть что-то увлекательное! 🎩✨

Оставайтесь любознательными и продолжайте приключение с ИИ! 🌟🚀
"""
    PROMO_CODE_NOT_FOUND_ERROR = """
🔍 <b>Ой, промокод не найден!</b>

Кажется, введённый вами промокод играет с нами в прятки. 🕵️‍♂️ Мы не смогли найти его в нашей системе.

🤔 Проверьте наличие опечаток и попробуйте ещё раз. Если всё ещё не получается, возможно, стоит поискать другой код или взглянуть на наши предложения в /subscribe и /buy за интересные сделки 🛍️

Не теряйте оптимизма и продолжайте веселиться с ИИ! 🚀🎈
"""
    PROMO_CODE_ALREADY_USED_ERROR = """
🚫 <b>Ой, дежавю!</b>

Похоже, вы уже использовали этот промокод. Это магия на один раз, и вы уже воспользовались ею! ✨🧙

Но не беспокойтесь! Вы можете ознакомиться с нашими последними предложениями в /subscribe или /buy. У нас всегда есть что-то новое в запасе! 🎉🔮

Продолжайте исследовать и пусть ИИ-сюрпризы продолжаются! 🤖
"""

    # AI
    MODE = """
🤖 Давайте посмотрим, что каждая модель может сделать для вас:

✉️ <b>ChatGPT3: Всесторонний коммуникатор</b>
- <i>От обычного разговора до глубоких бесед</i>: Идеален для чата на любую тему, от повседневной жизни до шуток.
- <i>Образовательный ассистент</i>: Помощь в выполнении домашних заданий, изучении языков или сложных тем, таких как программирование.
- <i>Личный тренер</i>: Мотивация, советы по фитнесу или даже руководство по медитации.
- <i>Творческий писатель</i>: Нужен пост, история или даже песня? ChatGPT3 создаст это за секунды.
- <i>Путешественник</i>: Спросите советы по путешествиям, местные кухни или исторические факты о вашем следующем направлении.
- <i>Бизнес-помощник</i>: Написание электронных писем, бизнес-планов или идей для маркетинга.
- <i>Ролевые игры</i>: Участие в творческих ролевых сценариях для развлечения или рассказа историй.
- <i>Краткие сводки</i>: Суммирование длинных статей или отчетов в лаконичный текст.

🧠 <b>ChatGPT4: Расширенный интеллект</b>
- <i>Глубокий анализ</i>: Идеально для детальных исследований, технических объяснений или исследования гипотетических сценариев.
- <i>Решение проблем</i>: Помощь в сложных математических задачах, ошибках программирования или научных вопросах.
- <i>Языковой эксперт</i>: Перевод сложных текстов или практика навыков разговорного языка на разных языках.
- <i>Творческий консультант</i>: Разработка идей для постов, диалогов для сценариев или исследование художественных концепций.
- <i>Здоровье и благополучие</i>: Обсуждение тем здоровья и психического благополучия на глубоком уровне.
- <i>Персонализированные рекомендации</i>: Получение рекомендаций по книгам, фильмам или путешествиям на основе ваших интересов.

🎨 <b>DALLE-3: Творческий гений</b>
- <i>Искусство по запросу</i>: Генерация уникальных изображений по описаниям - идеально для иллюстраторов или в поисках вдохновения.
- <i>Создатель рекламы</i>: Создание привлекательных изображений для рекламы или контента в социальных сетях.
- <i>Образовательный инструмент</i>: Визуализация сложных концепций для лучшего понимания в образовании.
- <i>Дизайн интерьера</i>: Получение идей для планировки комнат или тем декора.
- <i>Модный дизайн</i>: Создание дизайнов одежды или модных иллюстраций.
- <i>Персонализированные комиксы</i>: Создание комиксов или персонажей мультфильмов из ваших историй.
- <i>Макеты продуктов</i>: Создание макетов для идей продуктов или изобретений.

🤡 <b>Face Swap: Мастер развлечений</b>
- <i>Веселые переосмысления</i>: Посмотрите, как выглядели бы в разные исторические эпохи или в образе разных кино персонажей.
- <i>Персонализированные поздравления</i>: Создайте уникальные открытки или приглашения с персонализированными изображениями.
- <i>Ролевые игры</i>: Экспериментируйте с разными образами для ролевых игр или виртуальных встреч.
- <i>Мемы и создание Контента</i>: Оживите свои социальные сети смешными или фантазийными фотографиями с заменой лица.
- <i>Цифровые макияжи</i>: Экспериментируйте с новыми стрижками или стилями макияжа.
- <i>Смешение со знаменитостями</i>: Совместите свое лицо с знаменитостями для забавных сравнений.

Для смены модели выберите кнопку ниже 👇
"""
    ALREADY_MAKE_REQUEST = "Вы уже сделали запрос. Пожалуйста, подождите ⚠️"
    READY_FOR_NEW_REQUEST = "Вы можете задать следующий запрос 😌"
    CONTINUE_GENERATING = "Продолжить генерацию"
    REACHED_USAGE_LIMIT = """
<b>Ой-ой! 🚨</b>

Твоя квота на использование этой модели исчезла как фокусник Худини! 🎩
Но не переживай, у нас есть решение:
- Загляни в /buy или /subscribe, чтобы продолжить волшебство, или
- Переключись на другую модель AI через /mode

Приключения ждут! 🚀✨
"""
    IMAGE_SUCCESS = "✨ Вот ваше созданное изображение! 🎨"

    # Settings
    SETTINGS = "Настройки:"
    SHOW_NAME_OF_THE_CHAT = "Отображение названия чата в сообщениях"
    SHOW_USAGE_QUOTA_IN_MESSAGES = "Отображение квоты в сообщениях"
    TURN_ON_VOICE_MESSAGES_FROM_RESPONDS = "Включить голосовые сообщения для ответов"

    # Voice
    VOICE_MESSAGES_FORBIDDEN = """
🎙 <b>Упс! Кажется, ваш голос потерялся в AI-пространстве!</b>

Чтобы разблокировать чудо преобразования голоса в текст, просто воспользуйтесь волшебством команд /subscribe или /buy.

Давайте превратим эти голосовые сообщения в текст и продолжим общение! 🌟🔮
    """

    # Subscription
    MONTH_1 = "1 месяц"
    MONTHS_3 = "3 месяца"
    MONTHS_6 = "6 месяцев"
    DISCOUNT = "Скидка"
    NO_DISCOUNT = "Нет скидки"
    SUBSCRIPTION_SUCCESS = """
🎉 Ура! Теперь вы с нами! 🚀

Ваша подписка активирована, как белка на кофеине! 🐿️☕ Добро пожаловать в клуб потрясающих возможностей. Вот что вас ждет дальше:
- Перед вами открылся весь мир возможностей. 🌍✨
- Ваши AI-друзья уже готовы помогать вам. 🤖👍
- Приготовьтесь окунуться в море функций и веселья. 🌊🎉

Спасибо, что присоединились к нам в этом удивительном путешествии! Давайте творить чудеса! 🪄🌟
"""
    SUBSCRIPTION_RESET = """
🚀 <b>Квота подписки обновлена!</b>

Привет, путешественник в мире ИИ! 🌟
Угадай что? Твоя квота подписки только что была обновлена! Это как волшебное пополнение, только лучше, потому что это реальность. 🧙‍♂️
Впереди целый месяц веселья с ИИ. Общайся, твори, исследуй – нет предела! ✨

Продолжай раскрывать мощь ИИ и помни, мы здесь, чтобы сделать твои цифровые мечты реальностью. Давайте сделаем этот месяц лучше! 🤖💥
"""
    SUBSCRIPTION_END = """
🛑 <b>Подписка Истекла!</b>

Привет, энтузиаст ИИ! 🌟
Твоя подписка закончилась. Но не беспокойся, путешествие по миру ИИ еще не окончено! 🚀
Ты можешь возобновить свой магический доступ с помощью /subscribe и продолжить исследование вселенной ИИ. Или, если хочешь, загляни в /buy за индивидуальными пакетами, созданными специально для тебя. 🎁

Приключения в мире ИИ ждут! Подзарядись, соберись с мыслями, и давай продолжим этот захватывающий путь вместе. 🤖✨
"""

    # Package
    GPT3_REQUESTS = "✉️ GPT3 запросы"
    GPT3_REQUESTS_DESCRIPTION = "Разбудите мощь GPT 3 для остроумных бесед, умных советов и бесконечного веселья! 🤖✨"
    GPT4_REQUESTS = "🧠 GPT4 запросы"
    GPT4_REQUESTS_DESCRIPTION = "Исследуйте продвинутый интеллект GPT 4 для более глубоких открытий и прорывных бесед. 🧠🌟"
    THEMATIC_CHATS = "💬 Тематические чаты"
    THEMATIC_CHATS_DESCRIPTION = "Окунитесь в интересные темы с тематическими чатами, направляемыми AI в мире индивидуальных дискуссий. 📚🗨️"
    DALLE3_REQUESTS = "🖼 DALLE3 изображения"
    DALLE3_REQUESTS_DESCRIPTION = "Превратите свои идеи в искусство с помощью DALLE3 – там, где ваше воображение становится поразительной визуальной реальностью! 🎨🌈"
    FACE_SWAP_REQUESTS = "📷 Изображения с заменой лица"
    FACE_SWAP_REQUESTS_DESCRIPTION = "Погрузитесь в игровой мир замены лиц для смеха и удивления на каждом изображении! 😂🔄"
    ACCESS_TO_CATALOG = "🎭 Доступ к каталогу с ролями"
    ACCESS_TO_CATALOG_DESCRIPTION = "Откройте для себя вселенную специализированных AI-помощников с доступом к нашему эксклюзивному каталогу, где каждая роль адаптирована под ваши уникальные потребности и задачи"
    ANSWERS_AND_REQUESTS_WITH_VOICE_MESSAGES = "🎙 Ответы и запросы с голосовыми сообщениями"
    ANSWERS_AND_REQUESTS_WITH_VOICE_MESSAGES_DESCRIPTION = "Ощутите удобство и простоту голосового общения с нашим AI: отправляйте и получайте голосовые сообщения для более динамичного и выразительного взаимодействия"
    FAST_ANSWERS = "⚡ Быстрые ответы"
    FAST_ANSWERS_DESCRIPTION = "Функция 'Быстрые ответы' предлагает мгновенные, точные ответы AI, обеспечивая ваше преимущество в общении"
    MIN_ERROR = "Ой! Кажется, введенное число меньше нашего минимального порога. Пожалуйста, введите значение, соответствующее или превышающее минимально требуемое. Давайте попробуем еще раз! 🔄"
    VALUE_ERROR = "Упс! Похоже, это не число. 🤔 Не могли бы вы ввести числовое значение? Давайте попробуем еще раз! 🔢"
    PACKAGE_SUCCESS = """
🎉 <b>Ура! Оплата прошла успешно!</b> 💳

Ваша оплата прошла быстро, словно супергерой! 🦸‍ Вы успешно разблокировали невероятную мощь выбранного пакета. Готовьтесь к увлекательным приключениям с AI! 🎢

Помните, с большой силой приходит большая... ну вы знаете как говорят. Давайте творить чудеса! ✨🪄
"""

    # Catalog
    CATALOG = """
🎭 <b>Добро пожаловать в наш каталог ролей!</b> 🌟

Мечтали ли вы о специализированном AI-помощнике, созданном именно для вас? Наш каталог - это как волшебный гардероб, где каждая роль - уникальный наряд для ваших приключений в мире AI! 🧙‍♂️✨

Выбирайте из множества AI-персонажей, каждый со своими особенностями и знаниями. Вам нужен товарищ для мозгового штурма, творческая муза или фактический волшебник - у нас есть всё!

👉 Готовы встретить своего идеального помощника? Просто нажмите на кнопку ниже и пусть магия начнется! 🎩👇
"""
    CATALOG_FORBIDDEN_ERROR = """
🔒 <b>Ой! Похоже, вы попали в зону для VIP!</b> 🌟

Вы всего в одном клике от открытия нашего сокровища AI-ролей, но, кажется, у вас пока нет золотого ключика. Не волнуйтесь! Вы легко можете его получить.

🚀 Посетите /subscribe для замечательных вариантов подписки или перейдите в /buy, если хотите выбрать что-то из AI-деликатесов.

Как только вы будете готовы, наш каталог AI-чудес будет ждать вас – это ваш билет в необыкновенный мир возможностей AI! 🎫✨
"""

    # Chats
    DEFAULT_CHAT_TITLE = "Новый чат"
    SHOW_CHATS = "Показать чаты"
    CREATE_CHAT = "Создать новый чат"
    CREATE_CHAT_FORBIDDEN = """
🚫 <b>Ой-ой!</b>

Похоже, вы достигли предела по созданию новых чатов. Но не переживайте, мир бесконечных чатов всего в одном клике! 🌍✨

Перейдите в /subscribe или /buy, чтобы разблокировать возможность вести несколько чатов. Чем больше чатов, тем веселее! 🎉
"""
    CREATE_CHAT_SUCCESS = "💬 Чат создан! 🎉"
    TYPE_CHAT_NAME = "Напишите название чата"
    SWITCH_CHAT = "Переключиться между чатами"
    SWITCH_CHAT_FORBIDDEN = """
🔄 <b>Хотите переключиться? Подождите!</b> ⚙️

Сейчас вы находитесь в вашем единственном чате. Уютное место, но почему бы не расширить свои границы? 🌌

Чтобы перемещаться между разными тематическими чатами, просто получите ваш пропуск в /subscribe или /buy. Пусть начнется чат-путешествие! 🐇
"""
    SWITCH_CHAT_SUCCESS = "🔀 Чат успешно переключен! 🎉"
    DELETE_CHAT = "Удалить чат"
    DELETE_CHAT_FORBIDDEN = """
🗑️ <b>Удалить этот чат? Это про разговор в одиночестве!</b> 💬

Это ваш единственный чат-королевство, и королевству нужен свой король или королева! Удалить его - все равно что отменить свою собственную вечеринку. 🎈

А что если вместо этого добавить больше чатов в ваше царство? Посмотрите /subscribe или /buy, чтобы построить свою чат-империю! 👑
"""
    DELETE_CHAT_SUCCESS = "🗑️ Чат успешно удалён! 🎉"

    # Face swap
    CHOOSE_YOUR_PACKAGE = """
🌟 <b>Давайте творить с вашими фотографиями!</b>

<b>Первый шаг:</b> Выберите ваше приключение! 🚀

Готовы? Погружаемся в мир воображения! 🌈 Просто <b>выберите пакет</b> ниже и начните своё фотоприключение 👇
    """
    GENERATIONS_IN_PACKAGES_ENDED = """
🎨 <b>Ух ты, ты использовал все генерации в наших пакетах! Твоё творчество впечатляет!</b> 🌟

Что дальше?
- 📷 Отправь нам фото с лицами для замены лиц в Face Swap!
- 🔄 Или переключи модель через /mode, чтобы продолжить творить с другими AI-инструментами!

Время новых AI-открытий! 🚀
"""
    FACE_SWAP_MIN_ERROR = """
🤨 <b>Постойте, партнёр!</b>

Кажется, вы хотите запросить меньше одного изображения. В мире творчества нам нужно хотя бы одно, чтобы начать!

🌟 <b>Совет:</b> Введите число больше 0, чтобы начать волшебство. Давайте выпустим на волю творческие идеи!
"""
    FACE_SWAP_MAX_ERROR = """
🚀 <b>Ух ты, целимся высоко, вижу! Но, упс...</b>

Вы просите больше изображений, чем у нас есть.

🧐 <b>Как насчёт этого?</b> Давайте попробуем число в пределах лимита пакета!
"""

    ERROR = "Я получил ошибку"
    BACK = "Назад ◀️"
    CLOSE = "Закрыть 🚪"
    CANCEL = "Отменить ❌"
    APPROVE = "Подтвердить ✅"

    @staticmethod
    def profile(subscription_type: SubscriptionType,
                gender: UserGender,
                current_model: str,
                monthly_limits,
                additional_usage_quota) -> str:
        emojis = Subscription.get_emojis()

        if gender == UserGender.MALE:
            gender_info = f"Пол: {Russian.MALE} 👕"
        elif gender == UserGender.FEMALE:
            gender_info = f"Пол: {Russian.FEMALE} 👚"
        else:
            gender_info = f"Пол: {Russian.UNSPECIFIED}"

        return f"""
<b>Профиль</b> 👤

Тип подписки: {subscription_type} {emojis[subscription_type]}
{gender_info}
Валюта: RUB

Текущая модель: {current_model}
Поменять модель: /mode

✉️
GPT-3.5 запросов на месяц: {monthly_limits[Quota.GPT3]}/{SubscriptionLimit.LIMITS[subscription_type][Quota.GPT3]}
Дополнительные GPT-3.5 запросы: {additional_usage_quota[Quota.GPT3]}
GPT-4.0 запросов на месяц: {monthly_limits[Quota.GPT4]}/{SubscriptionLimit.LIMITS[subscription_type][Quota.GPT4]}
Дополнительные GPT-4.0 запросы: {additional_usage_quota[Quota.GPT4]}

🖼
DALL-E 3 изображений на месяц: {monthly_limits[Quota.DALLE3]}/{SubscriptionLimit.LIMITS[subscription_type][Quota.DALLE3]}
Дополнительные DALL-E 3 изображения: {additional_usage_quota[Quota.DALLE3]}

📷
Изображений с заменой лица на месяц: {monthly_limits[Quota.FACE_SWAP]}/{SubscriptionLimit.LIMITS[subscription_type][Quota.FACE_SWAP]}
Дополнительные изображения с заменой лица: {additional_usage_quota[Quota.FACE_SWAP]}

💬
Дополнительные чаты: {additional_usage_quota[Quota.ADDITIONAL_CHATS]}

Оформить подписку: /subscribe
Купить дополнительные запросы: /buy
"""

    @staticmethod
    def subscribe(currency: Currency):
        prices = Subscription.get_prices(currency)

        return f"""
🤖Готовы ускорить своё цифровое путешествие? Вот что мы предлагаем:

- <b>Standard</b> ⭐: Всего за {prices[SubscriptionType.STANDARD]} окунитесь в мир ИИ! Идеально для ежедневных размышлений, творческих вспышек и моментов любопытства. Общайтесь вовсю с ChatGPT 3, создавайте изображения из воздуха с DALLE-3 и меняйте лица быстрее, чем вы скажете "сыр"! 🧀

- <b>VIP</b> 🔥: Есть большие планы? За {prices[SubscriptionType.VIP]} вы откроете для себя более глубокие диалоги, более сложное создание изображений и доступ к более широкому ассортименту цифровых персонажей. Это настоящее удовольствие для опытного пользователя, предлагающее премиальную полосу на ИИ-шоссе. 🛣️

- <b>Platinum</b> 💎: Для ценителей, {prices[SubscriptionType.PLATINUM]} предоставляют ключи от королевства ИИ! Максимизируйте запросы ChatGPT 4, создавайте тематические чаты и получайте эксклюзивный доступ к последним инновациям в области ИИ. Это всё, что вы можете себе представить от ИИ, и даже больше! 🍽️

Выберите свой вариант и нажмите кнопку ниже, чтобы подписаться:
"""

    @staticmethod
    def choose_how_many_months_to_subscribe(subscription_type: SubscriptionType):
        emojis = Subscription.get_emojis()

        return f"""
Вы выбрали <b>{subscription_type}</b> {emojis[subscription_type]}

Пожалуйста, выберите период подписки, нажав на кнопку:
"""

    @staticmethod
    def cycles_subscribe():
        return {
            SubscriptionPeriod.MONTH1: Russian.MONTH_1,
            SubscriptionPeriod.MONTHS3: Russian.MONTHS_3,
            SubscriptionPeriod.MONTHS6: Russian.MONTHS_6,
        }

    @staticmethod
    def confirmation_subscribe(subscription_type: SubscriptionType, subscription_period: SubscriptionPeriod):
        cycles = Russian.cycles_subscribe()

        return f"Вы собираетесь активировать подписку на {cycles[subscription_period]}."

    # Package
    @staticmethod
    def buy():
        return """
🤖 <b>Добро пожаловать в магазин ИИ!</b> 🛍

Добро пожаловать в зону покупок, где каждое нажатие кнопки открывает мир чудес ИИ!
🧠 <b>ChatGPT3 & ChatGPT4</b>: Погрузитесь в глубокие, заставляющие задуматься разговоры. Ваши новые ИИ-друзья уже ждут!
🎨 <b>Волшебство DALLE-3</b>: Превращайте идеи в потрясающие визуализации. Это как рисование с помощью ИИ!
👤 <b>Веселье с заменой лиц</b>: Играйте с идентичностью на изображениях. Это ещё никогда не было так захватывающе!
🗣️ <b>Голосовые сообщения</b>: Говорите вслух! Общение с ИИ ещё никогда не звучало так хорошо.
💬 <b>Тематические чаты</b>: Погрузитесь в специализированные темы и исследуйте посвящённые им чаты.
🎭 <b>Доступ к каталогу ролей</b>: Нужен определённый ассистент? Просмотрите нашу коллекцию и найдите своё идеальное сочетание ИИ.
⚡ <b>Быстрые сообщения</b>: Быстро, эффективно и всегда точно. Общение с ИИ на скорости молнии.

Нажмите кнопку и отправляйтесь в необыкновенное путешествие с ИИ! Пора переопределить возможное. 🌌🛍️
"""

    @staticmethod
    def choose_min(package_type: PackageType):
        return f"""
🚀 Замечательно!

Вы выбрали пакет <b>{package_type}</b>
🌟 Пожалуйста, <b>введите количество запросов</b>, которое вы хотели бы выбрать
"""

    # Chats
    @staticmethod
    def chats(current_chat_name: str, total_chats: int, available_to_create_chats: int):
        return f"""
🗨️ <b>Текущий чат: {current_chat_name}</b> 🌟

Добро пожаловать в динамичный мир чатов, управляемых ИИ! Вот что вы можете сделать:

- Создать новые тематические чаты: Погрузитесь в сосредоточенные обсуждения, соответствующие вашим интересам.
- Переключаться между чатами: Без усилий навигируйте по вашим различным чатам.
- Удалять чаты: Очистите пространство, удалив чаты, которые вам больше не нужны.

📈 <b>Всего чатов: {total_chats} | Доступно для создания чатов: {available_to_create_chats}</b>

Готовы настроить свой опыт чата? Исследуйте предложенные ниже опции и начните общение! 🚀👇
"""

    # Face swap
    @staticmethod
    def choose_face_swap_package(name: str, available_images, total_images: int, used_images: int) -> str:
        remain_images = total_images - used_images
        return f"""
<b>{name}</b>

У вас есть целое сокровище из <b>{total_images} изображений</b> в вашем пакете, готовое раскрыть ваше творчество! 🌟

🌠 <b>Доступные генерации</b>: {available_images} изображений. Нужно больше? Ознакомьтесь с /buy и /subscribe!
🔍 <b>Использовано</b>: {used_images} изображений. {'Вау, вы на волне!' if used_images > 0 else ''}
🚀 <b>Осталось</b>: {remain_images} изображений. {'Вы уже использовали их все' if remain_images == 0 else 'Столько ещё возможностей'}!

📝 <b>Напишите, сколько смен лиц вы хотите сделать, или выберите из кнопок быстрого выбора ниже</b>. Мир трансформаций лиц ждет вас! 🎭🔄
"""

    @staticmethod
    def face_swap_package_forbidden(available_images: int):
        return f"""
🔔 <b>Упс, небольшая проблема!</b> 🚧

Похоже, у вас осталось только <b>{available_images} генераций</b> в вашем арсенале.

💡 <b>Совет</b>: Иногда меньше — это больше! Попробуйте ввести меньшее количество, или воспользуйтесь /buy и /subscribe для неограниченных возможностей!
"""

    @staticmethod
    def wait_for_another_request(seconds: int) -> str:
        return f"Пожалуйста, подождите еще {seconds} сек. перед отправкой следующего запроса ⏳"

    @staticmethod
    def processing_request_text():
        texts = [
            "Сейчас консультируюсь с моим цифровым хрустальным шаром, чтобы найти лучший ответ... 🔮",
            "Минуточку, тренирую своих хомячков, чтобы они сгенерировали ваш ответ... 🐹",
            "Роюсь в своей цифровой библиотеке в поисках идеального ответа. Немного терпения... 📚",
            "Подождите, я вызываю своего внутреннего гуру ИИ для вашего ответа... 🧘",
            "Подождите, пока я консультируюсь с повелителями интернета для вашего ответа... 👾",
            "Собираю мудрость веков... или, по крайней мере, то, что могу найти в интернете... 🌐",
            "Секундочку, надеваю свою шляпу для размышлений... А, вот так лучше. Теперь давайте посмотрим... 🎩",
            "Закатываю свои виртуальные рукава и приступаю к делу. Ваш ответ уже на подходе... 💪",
            "Работаю на полную мощность! Мои ИИ-шестеренки крутятся, чтобы принести ваш ответ... 🚂",
            "Погружаюсь в океан данных, чтобы выловить ваш ответ. Скоро вернусь... 🌊🎣",
            "Консультируюсь со своими виртуальными эльфами. Обычно они отлично находят ответы... 🧝",
            "Включаю сверхсветовой привод для быстрого поиска ответа. Держитесь крепче... 🚀",
            "Нахожусь на кухне и готовлю свежую партию ответов. Этот будет вкусным... 🍳",
            "Совершаю быструю поездку в облако и обратно. Надеюсь принести несколько умных капель информации... ☁️",
            "Сажаю ваш вопрос в моем цифровом саду. Посмотрим, что вырастет... 🌱🤖"
        ]

        return random.choice(texts)

    @staticmethod
    def processing_request_image():
        texts = [
            "Собираю звездную пыль для создания вашего космического шедевра... 🌌",
            "Мешаю палитру цифровых красок для вашего шедевра... 🎨",
            "Окунаюсь в виртуальные чернила, чтобы набросать ваше видение... 🖌️",
            "Призываю музы AI для вдохновляющего рисунка... 🌠",
            "Создаю пиксели до совершенства, мгновение... 👁️🎭",
            "Готовлю визуальный пир для ваших глаз... 🍽️👀",
            "Консультируюсь с цифровым Да Винчи по вашему артистическому запросу... 🎭",
            "Протираю пыль с цифрового мольберта для вашего творческого запроса... 🖼️🖌️",
            "Творю визуальное заклинание в котле AI... 🧙‍🔮",
            "Активирую виртуальный холст. Готовьтесь к искусству... 🖼️",
            "Собираю ваши идеи в галерею пикселей... 🖼️👨‍🎨",
            "Отправляюсь в цифровое сафари, чтобы запечатлеть ваше художественное видение... 🦁🎨",
            "Запускаю AI-двигатели искусства, ожидайте... 🏎️💨",
            "Окунаюсь в бассейн цифрового воображения... 🏊‍💭",
            "Готовлю визуальную симфонию на кухне AI... 🍳🎼"
        ]

        return random.choice(texts)

    @staticmethod
    def processing_request_face_swap():
        texts = [
            "Переношусь в измерение смены лиц... 🌌👤",
            "Смешиваю и подбираю лица, как цифровой Пикассо... 🧑‍🎨🖼️",
            "Меняю лица быстрее, чем хамелеон меняет цвета... 🦎🌈",
            "Пробуждаю магию слияния лиц... ✨👥",
            "Произвожу алхимию лиц, меняю идентичность... 🧙‍🧬",
            "Завожу машину для смены лиц... 🤖🔀",
            "Готовлю зелье для трансформации лица... 🧪👩‍🔬",
            "Творю чары в мире заклинаний лиц... 🧚‍🎭️",
            "Руковожу симфонией черт лица... 🎼👩‍🎤👨‍🎤",
            "Леплю новые лица в моей цифровой арт-студии... 🎨👩‍🎨",
            "Варю котел волшебства смены лиц... 🧙‍🔮",
            "Строю лица, как великий архитектор... 🏗️👷‍",
            "Начинаю мистический поиск идеального сочетания лиц... 🗺️🔍",
            "Запускаю ракету приключений по смене лиц... 🚀👨‍🚀👩‍🚀",
            "Отправляюсь в галактическое путешествие смены лиц... 🌌👽"
        ]

        return random.choice(texts)
