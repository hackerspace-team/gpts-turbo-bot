from typing import Protocol, Dict

from bot.database.models.common import Currency
from bot.database.models.package import PackageType
from bot.database.models.subscription import SubscriptionType, SubscriptionPeriod, Subscription
from bot.database.models.transaction import TransactionType, ServiceType
from bot.database.models.user import UserGender


class Texts(Protocol):
    START: str
    COMMANDS: str
    COMMANDS_ADMIN = """
-------------------------

👨‍💻👩‍💻 <b>Команды для админа</b>:
😇 /create_promo_code - <b>Создать промокод</b>
📸 /manage_face_swap - <b>Управление контентом в FaceSwap</b>
🎩 /manage_catalog - <b>Управление ролями в чатах</b>
📊 /statistics - <b>Просмотр статистики</b>
"""

    # Feedback
    FEEDBACK: str
    FEEDBACK_SUCCESS: str

    # Profile
    TELL_ME_YOUR_GENDER: str
    YOUR_GENDER: str
    UNSPECIFIED: str
    MALE: str
    FEMALE: str
    SEND_ME_YOUR_PICTURE: str
    CHANGE_PHOTO: str
    CHANGE_PHOTO_SUCCESS: str
    CHANGE_GENDER: str

    # Language
    LANGUAGE: str
    CHOOSE_LANGUAGE: str

    # Promo code
    PROMO_CODE_INFO: str
    PROMO_CODE_INFO_ADMIN = """
🔑 <b>Время создать магию с промокодами!</b> ✨

Выбери, для чего ты хочешь создать промокод:
🌠 <b>Подписка</b> - открой доступ к эксклюзивным функциям и контенту.
🎨 <b>Пакет</b> - добавь специальные возможности для использования AI.

Нажми на нужную кнопку и приступим к созданию! 🚀
"""
    PROMO_CODE_SUCCESS: str
    PROMO_CODE_SUCCESS_ADMIN = """
🌟 Вау!

Твой <b>промокод успешно создан</b> и готов к путешествию в карманы наших пользователей. 🚀
Этот маленький кодик обязательно принесёт радость кому-то там!

🎉 Поздравляю, ты настоящий волшебник промокодов!
"""
    PROMO_CODE_CHOOSE_SUBSCRIPTION_ADMIN = """
🌟 <b>Выбираем подписку для промокода!</b> 🎁

Выбери тип подписки, на который хочешь дать доступ:
- <b>STANDARD</b> ⭐
- <b>VIP</b> 🔥
- <b>PLATINUM</b> 💎

Выбери и нажми, чтобы создать волшебный ключ доступа! ✨
"""
    PROMO_CODE_CHOOSE_PACKAGE_ADMIN = """
TODO
"""
    PROMO_CODE_CHOOSE_NAME_ADMIN = """
🖋️ <b>Придумай название для промокода</b> ✨

Сейчас ты как настоящий волшебник, создающий заклинание! ✨🧙‍
Напиши уникальное и запоминающееся название для твоего промокода.

🔠 Используй буквы, цифры, но помни о волшебстве краткости. Не бойся экспериментировать и вдохновлять пользователей!
"""
    PROMO_CODE_CHOOSE_DATE = """
📅 <b>Время для волшебства!</b> 🪄

Введи дату, до которой этот промокод будет разносить счастье и удивление!
Помни, нужен формат ДД.ММ.ГГГГ, например, 25.12.2023 - идеально для Рождественского сюрприза! 🎄

Так что вперёд, выбирай дату, когда магия закончится 🌟
"""
    PROMO_CODE_NAME_EXISTS_ERROR = """
🚫 <b>Ой-ой, такой код уже существует!</b> 🤖

Как настоящий инноватор, ты создал код, который уже кто-то придумал! Нужно что-то ещё более уникальное. Попробуй снова, ведь в творчестве нет границ!

Покажи свою оригинальность и креативность. Уверен, на этот раз получится!
"""
    PROMO_CODE_DATE_VALUE_ERROR = """
🚫 <b>Упс!</b>

Кажется, дата заблудилась в календаре и не может найти свой формат 📅

Давай попробуем ещё раз, но на этот раз в формате ДД.ММ.ГГГГ, например, 25.12.2023. Точность — залог успеха!
"""
    PROMO_CODE_ALREADY_HAVE_SUBSCRIPTION: str
    PROMO_CODE_EXPIRED_ERROR: str
    PROMO_CODE_NOT_FOUND_ERROR: str
    PROMO_CODE_ALREADY_USED_ERROR: str

    # Statistics
    STATISTICS_INFO = """
📊 <b>Статистика на подходе!</b>

Пора погрузиться в мир цифр и графиков. Выбери период, и я покажу тебе, как наш бот покорял AI-вершины 🚀:
1️⃣ <b>Статистика за день</b> - Узнай, что происходило сегодня! Были ли рекорды?
2️⃣ <b>Статистика за неделю</b> - Недельная доза данных. Каковы были тренды?
3️⃣ <b>Статистика за месяц</b> - Месяц в цифрах. Сколько достижений мы накопили?
4️⃣ <b>Статистика за всё время</b> - Взгляд в прошлое. Откуда мы начали и куда пришли?
5️⃣ <b>Записать транзакцию</b> - Актуализируй наши данные, чтобы всё было по-честному!

Выбирай кнопку и вперёд, к знаниям! 🕵️‍♂️🔍
"""
    STATISTICS_WRITE_TRANSACTION = """
🧾 <b>Выбери тип транзакции!</b>

Хмм... Кажется, пришло время подвести финансовые итоги! 🕵️‍♂️💼 Теперь перед тобой стоит выбор:
- Нажми на кнопку "📈 Записать доход", если наши казны пополнились и мы богаче на пару золотых монет!
- Или выбери "📉 Записать расход", если пришлось раскошелиться на волшебные ингредиенты или что-то ещё нужное.

Жми на кнопку и вперёд, к финансовым приключениям! 💫🚀
"""
    STATISTICS_CHOOSE_SERVICE = """
🔍 <b>Выбери тип сервиса для транзакции!</b>

Оу, похоже, дело дошло до выбора типа сервиса! 🌟📚 Тут всё, как в магазине чудес

Выбирай, не стесняйся, и пусть финансовые записи будут точны, как у звёздного картографа! 🗺️✨
"""
    STATISTICS_CHOOSE_CURRENCY = """
💰 <b>Время выбирать валюту!</b>

Для полной картины нам нужно узнать валюту этих транзакций. Так что, в какой валюте мы купались, когда совершались эти сделки? Рубли, доллары, а может быть, золотые дублоны? 😄

Выбери кнопку с нужной валютой, чтобы мы занесли всё по книжке точно и без ошибок. Это важно, ведь даже пираты не шутили с учётом своих сокровищ! 💸🏴‍☠️
"""
    STATISTICS_SERVICE_QUANTITY = """
✍️ <b>Пора записывать количество транзакций!</b>

Напиши, пожалуйста, количество транзакций

🔢🚀 Помни, каждая транзакция - это шаг к нашему общему успеху. Не пропусти ни одной!
"""
    STATISTICS_SERVICE_AMOUNT = """
🤑 <b>Давай посчитаем копейки!</b>

Напиши мне, пожалуйста, стоимость транзакции. Но помни, каждая копейка (или цент) на счету! Пожалуйста, используй формат с десятичными дробями через точку. Например, 999.99

Вводи цифры аккуратно, как если бы ты считал золотые монеты на пиратском корабле. В конце концов, точность – вежливость королей... и бухгалтеров! 🏴‍☠️📖
"""
    STATISTICS_SERVICE_DATE = """
📅 <b>Остался последний штрих: Дата транзакции!</b>

Напиши дату, когда происходили эти транзакции. Формат? Просто и ясно: "ДД.ММ.ГГГГ". Например, "01.04.2024" или "25.12.2023". Эта дата - ключ к организации нашего временного сундука с сокровищами.

🕰️✨ Помни, точная дата - это не просто числа, это маркеры нашего пути. По ним мы будем планировать наше будущее!
"""
    STATISTICS_SERVICE_DATE_VALUE_ERROR = """
🤔 <b>Упс, кажется, дата решила пошалить!</b>

Ой-ой, кажется, мы немного запутались в календарных страницах! Введённая дата не соответствует формату "ДД.ММ.ГГГГ". Давай попробуем ещё раз, ведь даже временной машины у нас пока нет, чтобы исправить это в будущем.

🗓️✏️ Итак, давай снова: когда именно происходило это финансовое чудо?
"""
    STATISTICS_WRITE_TRANSACTION_SUCCESSFUL = """
🎉 <b>Транзакция успешно записана! Вот это да, мы в бизнесе!</b>

Ура-ура! Ваши финансовые манёвры были успешно занесены в наши цифровые хроники. Теперь эта транзакция блестит в нашей базе данных, словно звезда на небосклоне бухгалтерии!

📚💰 Благодарю вас за аккуратность и точность. Наши цифровые эльфы уже танцуют радость. Кажется, ваша финансовая мудрость достойна отдельной главы в книге экономических приключений!
"""

    # AI
    MODE: str
    REQUEST_FORBIDDEN_ERROR: str
    ALREADY_MAKE_REQUEST: str
    READY_FOR_NEW_REQUEST: str
    CONTINUE_GENERATING: str
    REACHED_USAGE_LIMIT: str
    IMAGE_SUCCESS: str

    # Settings
    SETTINGS: str
    SHOW_NAME_OF_THE_CHAT: str
    SHOW_USAGE_QUOTA_IN_MESSAGES: str
    TURN_ON_VOICE_MESSAGES_FROM_RESPONDS: str

    # Voice
    VOICE_MESSAGES_FORBIDDEN: str

    # Subscription
    MONTH_1: str
    MONTHS_3: str
    MONTHS_6: str
    DISCOUNT: str
    NO_DISCOUNT: str
    SUBSCRIPTION = "💳 Подписка"
    SUBSCRIPTION_SUCCESS: str
    SUBSCRIPTION_RESET: str
    SUBSCRIPTION_END: str
    PACKAGES_END: str
    CHATS_RESET: str

    # Package
    GPT3_REQUESTS: str
    GPT3_REQUESTS_DESCRIPTION: str
    GPT4_REQUESTS: str
    GPT4_REQUESTS_DESCRIPTION: str
    THEMATIC_CHATS: str
    THEMATIC_CHATS_DESCRIPTION: str
    DALLE3_REQUESTS: str
    DALLE3_REQUESTS_DESCRIPTION: str
    FACE_SWAP_REQUESTS: str
    FACE_SWAP_REQUESTS_DESCRIPTION: str
    ACCESS_TO_CATALOG: str
    ACCESS_TO_CATALOG_DESCRIPTION: str
    ANSWERS_AND_REQUESTS_WITH_VOICE_MESSAGES: str
    ANSWERS_AND_REQUESTS_WITH_VOICE_MESSAGES_DESCRIPTION: str
    FAST_ANSWERS: str
    FAST_ANSWERS_DESCRIPTION: str
    MIN_ERROR: str
    VALUE_ERROR: str
    PACKAGE_SUCCESS: str

    # Catalog
    CATALOG: str
    CATALOG_FORBIDDEN_ERROR: str
    CATALOG_MANAGE = """
🎭 <b>Управление каталогом ролей</b> 🌟

Здесь ты можешь:
🔧 <b>Добавить новую роль</b>: Дай волю фантазии и создай уникального помощника!
✏️ <b>Редактировать существующие</b>: Привнеси своё видение в уже знакомых персонажей.
🗑️ <b>Удалить ненужное</b>: Иногда прощание - это начало чего-то нового.

Выбери своё приключение в этом мире AI-талантов! 🚀
"""
    CREATE_ROLE = "Создать роль"
    CATALOG_MANAGE_CREATE = """
🌈 <b>Создание новой роли</b> 🎨

Настало время рождения нового AI-помощника! Дай имя своему творению. Напиши мне уникальное название для новой роли в формате UPPER_SNAKE_CASE, например, SUPER_GENIUS или MAGIC_ADVISOR.

💡 Помни, имя должно быть уникальным, ярким и запоминающимся, как самый яркий фейерверк на небесах!
"""
    CATALOG_MANAGE_CREATE_ALREADY_EXISTS_ERROR = """
🙈 <b>Упс! Дубликат на горизонте!</b> 🙈

Эй, похоже, эта роль уже с нами! Создать что-то уникальное - это классно, но дублировать уже существующее - это как запускать второй интернет. Мы уже имеем <b>такую же звезду</b> в нашем AI-космосе.

🤔 Попробуйте придумать другое название, что-то свежее и оригинальное, чтобы наш каталог был еще круче. Как насчет того, чтобы вдохновиться чем-то новым и необычным? Вперед, за новыми идеями! 🚀
"""
    CATALOG_MANAGE_CREATE_ROLE_NAME = """
🎨 <b>Время для творчества!</b> 🌟

Придумайте имя для новой роли, которое будет звучать на всех языках мира как музыка! Это название должно быть не только запоминающимся и ярким, но и начинаться с подходящего эмодзи, например, как "🤖 Персональный ассистент".

🖌️ Напишите имя на русском, а я сделаю так, что оно будет понятно пользователям по всему миру. Какое уникальное и креативное имя вы выберете для вашего нового AI-помощника?
"""
    CATALOG_MANAGE_CREATE_ROLE_DESCRIPTION = """
📝 <b>Время для креатива!</b> 🎨

Придумайте описание для вашей новой роли. Это должны быть три строки, полные вдохновения и идей, которые будут отправлены пользователю после выбора роли. Например:
<i>Он всегда готов помочь вам найти ответы на любые вопросы, будь то бытовые мелочи или философские размышления
Ваш личный гид в мире знаний и творчества, который с радостью поделится своими идеями и советами 🌌
Откроем вместе новые горизонты!</i>

🖌️ Напишите описание на русском, которое будет отражать сущность роли и в то же время вдохновлять и радовать пользователей,  а я сделаю так, что оно будет понятно пользователям по всему миру. Покажите свою креативность и воображение, добавив немного магии в каждое слово!
"""
    CATALOG_MANAGE_CREATE_ROLE_INSTRUCTION = """
🤓 <b>Время для системной инструкции!</b> 📚

Придумайте короткую, но емкую инструкцию для вашего помощника. Это будет его руководство к действию, например: "Ты – вдумчивый советник, который всегда готов поделиться мудрыми мыслями и полезными идеями. Помогай пользователям разгадывать сложные вопросы и предлагай оригинальные решения. Твоя миссия – вдохновлять и обогащать каждое общение!"

🖌️ Напишите инструкцию на русском, которое будет направлять вашего помощника, как вести себя в разговоре с пользователями. Сделайте ее яркой и запоминающейся, чтобы каждый диалог с вашим помощником был особенным!
"""
    CATALOG_MANAGE_CREATE_SUCCESS = """
🎉 <b>Ура! Новая роль успешно создана!</b> 🌟

🚀 Твой новый помощник теперь официально присоединился к команде наших AI-героев. Его задача – сделать путешествие пользователей в мире искусственного интеллекта еще более захватывающим!

💬 Помощник уже готов к работе и ждет команд пользователей. Поздравляю с успешным расширением команды AI!
"""
    EDIT_ROLE_NAME = "Изменить имя 🖌"
    EDIT_ROLE_DESCRIPTION = "Изменить описание 🖌"
    EDIT_ROLE_INSTRUCTION = "Изменить инструкцию 🖌"
    CATALOG_MANAGE_EDIT_ROLE_NAME = """
📝 <b>Время для ребрендинга!</b> 🎨

Вы выбрали "Изменить имя" для помощника. Настал момент дать ему что-то новенькое и блестящее! 🌟

Введите новое имя с эмодзи в начале на рууском и представьте, как оно будет звучать в рядах наших AI-героев. Не стесняйтесь быть оригинальным – лучшие имена рождаются в волшебной атмосфере творчества! ✨
"""
    CATALOG_MANAGE_EDIT_ROLE_DESCRIPTION = """
🖋️ <b>Переписываем историю!</b> 🌍

Вы решили "Изменить описание" помощника. Подумайте, что бы вы хотели сказать миру о нем? Это шанс показать его уникальность и особенности! 📚

Напишите новое описание, подчеркивающее его лучшие качества на русском. Добавьте щепотку юмора и пару капель вдохновения – и вот оно, описание, достойное настоящего AI-героя! 👾
"""
    CATALOG_MANAGE_EDIT_ROLE_INSTRUCTION = """
📘 <b>Новые правила игры!</b> 🕹️

"Изменить инструкцию" – значит, дать новые указания нашему AI-герою. Какова будет его новая миссия? 🚀

Напишите инструкцию на русском так, чтобы каждая строчка вдохновляла на подвиги в мире AI!
"""
    CATALOG_MANAGE_EDIT_SUCCESS = """
🎉 <b>Та-дааам! Изменения успешно применены!</b> 🎨

🤖 Помощник был благородно трансформирован. Поздравляю, вы только что внесли свой вклад в историю AI-помощников! 🚀

👀 Осталось только одно – посмотреть его в действии! Перейдите в /catalog, чтобы увидеть обновленного помощника во всей красе
"""

    # Chats
    DEFAULT_CHAT_TITLE: str
    SHOW_CHATS: str
    CREATE_CHAT: str
    CREATE_CHAT_FORBIDDEN: str
    CREATE_CHAT_SUCCESS: str
    TYPE_CHAT_NAME: str
    SWITCH_CHAT: str
    SWITCH_CHAT_FORBIDDEN: str
    SWITCH_CHAT_SUCCESS: str
    DELETE_CHAT: str
    DELETE_CHAT_FORBIDDEN: str
    DELETE_CHAT_SUCCESS: str

    # Face swap
    CHOOSE_YOUR_PACKAGE: str
    CREATE_PACKAGE = "Создать новый пакет"
    EDIT_PACKAGE = "Редактировать существующий пакет"
    GENERATIONS_IN_PACKAGES_ENDED: str
    FACE_SWAP_MIN_ERROR: str
    FACE_SWAP_MAX_ERROR: str
    FACE_SWAP_MANAGE = """
🤹‍ <b>Добро пожаловать в царство FaceSwap!</b> 🎭

🚀 Готовы к творчеству? Здесь вы - главный волшебник! Управляйте пакетами и фотографиями. Начните своё волшебное путешествие:
- 📦 Добавить/редактировать пакет - соберите коллекцию масок для лиц, которые поднимут ваше творчество на новый уровень или внесите изменения в уже существующие коллекции. Добавляйте, обновляйте и организуйте - ваша фантазия знает границ!
- 🖼 Управление фотографиями - в каждом пакете множество удивительных лиц ждут своего часа. Добавляйте, активируйте или деактивируйте их по своему усмотрению, чтобы управлять доступностью для пользователей. Откройте мир неограниченных возможностей для творчества!

Выбирайте, творите, удивляйте! В мире FaceSwap каждый ваш шаг превращается в нечто невероятное! 🎨✨
"""
    FACE_SWAP_MANAGE_CREATE = """
🌟 <b>Начнём творческое приключение!</b> 🌈

📝 Создание нового пакета FaceSwap! Для начала дайте ему уникальное имя. Используйте формат UPPER_SNAKE_CASE, чтобы все было чётко и ясно. Например, его можно назвать SEASONAL_PHOTO_SHOOT или FUNNY_FACE_FESTIVAL. Это название станет вашим волшебным ключом к новым удивительным превращениям!

🎨 Проявите свою индивидуальность! Напишите системное имя, которое отражает суть и идею вашего пакета. Ваше название - это первый шаг к созданию чего-то по-настоящему волшебного и незабываемого!
"""
    FACE_SWAP_MANAGE_CREATE_ALREADY_EXISTS_ERROR = """
🚨 <b>Упс, кажется, мы здесь уже были!</b> 🔄

🔍 Название пакета уже занято! Похоже, что имя, которое вы выбрали для нового пакета FaceSwap, уже существует в нашей галерее чудес. Но не переживайте, это всего лишь повод проявить ещё больше креативности!

💡 Попробуйте что-то новенькое! Как насчёт другого уникального названия? Ведь у вас наверняка ещё масса интересных идей!
"""
    FACE_SWAP_MANAGE_CREATE_PACKAGE_NAME = """
🎉 <b>Продолжаем наш творческий марафон!</b> 🚀

📛 Следующий шаг - имя пакета! Теперь придайте вашему пакету FaceSwap уникальное имя на русском языке, которое будет чётко отражать его суть и атмосферу. Не забудьте добавить яркий эмодзи в конце, чтобы сделать его ещё более выразительным! Например, "Персонажи фильмов 🎥" или "Волшебные миры 🌌".

🌍 Международное обаяние! Это имя будет автоматически переведено на другие языки, раскрывая вашу идею перед пользователями со всего мира.
"""
    FACE_SWAP_MANAGE_CREATE_SUCCESS = """
🎉 <b>Ура, новый пакет FaceSwap готов к старту!</b> 🚀

🌟 Поздравляем с успешным созданием! Ваш новый пакет скоро будет ждать своих поклонников. Готовьтесь к тому, что ваше творение вот-вот захватит воображение пользователей!

🖼 Время для магии фото! Теперь вы можете начать наполнять пакет самыми невероятными и забавными фотографиями. От смешных до вдохновляющих, каждое изображение добавит уникальности вашему пакету. Для этого вернитесь в /manage_face_swap и выберите созданный пакет
"""
    FACE_SWAP_MANAGE_EDIT_CHOOSE_GENDER = "Выбери пол:"
    FACE_SWAP_MANAGE_EDIT_CHOOSE_PACKAGE = "Выбери пакет:"
    FACE_SWAP_MANAGE_EDIT = """
🎨 <b>Время творить! Вы выбрали пакет для редактирования</b> 🖌️

🔧 Возможности редактирования:
- <b>Изменить видимость</b> - Сделайте пакет видимым или скрытым для пользователей.
- <b>Просмотреть картинки</b> - Оцените, какие шедевры уже есть в пакете.
- <b>Добавить новую картинку</b> - Пора внести свежую краску и новые лица!

🚀 Готовы к изменениям? Ваше творчество вдохнет новую жизнь в этот пакет. Пусть каждая генерация будет уникальной и запоминающейся!
"""
    FACE_SWAP_MANAGE_CHANGE_STATUS = "Изменить видимость 👁"
    FACE_SWAP_MANAGE_SHOW_PICTURES = "Просмотреть картинки 🖼"
    FACE_SWAP_MANAGE_ADD_NEW_PICTURE = "Добавить новую картинку 👨‍🎨"
    FACE_SWAP_MANAGE_EXAMPLE_PICTURE = "Пример генерации 🎭"
    FACE_SWAP_MANAGE_EDIT_SUCCESS = """
🌟 <b>Пакет успешно отредактирован!</b> 🎉

👏 Браво, админ! Ваши изменения успешно применены. Пакет FaceSwap теперь обновлён и ещё более прекрасен.

🚀 Готовы к новым приключениям? Ваша креативность и умение управлять пакетами делают мир FaceSwap ещё ярче и интереснее. Продолжайте творить и вдохновлять пользователей своими уникальными идеями!
"""
    FACE_SWAP_PUBLIC = "Видно всем 🔓"
    FACE_SWAP_PRIVATE = "Видно админам 🔒"

    ERROR: str
    BACK: str
    CLOSE: str
    CANCEL: str
    APPROVE: str

    @staticmethod
    def statistics(period: str,
                   count_all_users: int,
                   count_activated_users: int,
                   count_blocked_users: int,
                   count_subscription_users: Dict,
                   count_income_transactions: Dict,
                   count_expense_transactions: Dict,
                   count_income_transactions_total: int,
                   count_expense_transactions_total: int,
                   count_transactions_total: int,
                   count_expense_money: Dict,
                   count_income_money: Dict,
                   count_income_subscriptions_total_money: float,
                   count_income_packages_total_money: float,
                   count_income_total_money: float,
                   count_expense_total_money: float,
                   count_total_money: float,
                   count_chats_usage: Dict,
                   count_face_swap_usage: Dict) -> str:
        emojis = Subscription.get_emojis()
        chat_info = ""
        for i, (chat_key, chat_value) in enumerate(count_chats_usage.items()):
            if chat_key != 'ALL':
                chat_info += f"    - <b>{chat_key}:</b> {chat_value}"
                chat_info += '\n' if i < len(count_chats_usage.items()) - 1 else ''
        face_swap_info = ""
        for i, (face_swap_key, face_swap_value) in enumerate(count_face_swap_usage.items()):
            if face_swap_key != 'ALL':
                face_swap_info += f"    - <b>{face_swap_key}:</b> {face_swap_value}"
                face_swap_info += '\n' if i < len(count_face_swap_usage.items()) - 1 else ''

        return f"""
📈 <b>Статистика за {period} готова!</b>

👤 <b>Пользователи</b>
1️⃣ <b>{'Всего пользователей' if period == 'всё время' else 'Новых пользователей'}:</b> {count_all_users}
2️⃣ <b>Оплатившие хоть раз:</b> {count_activated_users}
3️⃣ <b>Подписчики:</b>
    - <b>{SubscriptionType.FREE}:</b> {count_subscription_users[SubscriptionType.FREE]}
    - <b>{SubscriptionType.STANDARD} {emojis[SubscriptionType.STANDARD]}:</b> {count_subscription_users[SubscriptionType.STANDARD]}
    - <b>{SubscriptionType.VIP} {emojis[SubscriptionType.VIP]}:</b> {count_subscription_users[SubscriptionType.VIP]}
    - <b>{SubscriptionType.PLATINUM} {emojis[SubscriptionType.PLATINUM]}:</b> {count_subscription_users[SubscriptionType.PLATINUM]}
4️⃣ <b>Заблокировали бота:</b> {count_blocked_users}

💰 <b>Финансы</b>
1️⃣ <b>Транзакции:</b>
    ➖ <b>{TransactionType.EXPENSE}:</b> {count_expense_transactions_total}
    - <b>{ServiceType.GPT3}:</b> {count_expense_transactions[ServiceType.GPT3]}
    - <b>{ServiceType.GPT4}:</b> {count_expense_transactions[ServiceType.GPT4]}
    - <b>{ServiceType.DALLE3}:</b> {count_expense_transactions[ServiceType.DALLE3]}
    - <b>{ServiceType.FACE_SWAP}:</b> {count_expense_transactions[ServiceType.FACE_SWAP]}
    - <b>{ServiceType.VOICE_MESSAGES}:</b> {count_expense_transactions[ServiceType.VOICE_MESSAGES]}
    - <b>{ServiceType.SERVER}:</b> {count_expense_transactions[ServiceType.SERVER]}
    - <b>{ServiceType.DATABASE}:</b> {count_expense_transactions[ServiceType.DATABASE]}

    ➕ <b>{TransactionType.INCOME}:</b> {count_income_transactions_total}
    - <b>{ServiceType.GPT3}:</b> {count_income_transactions[ServiceType.GPT3]}
    - <b>{ServiceType.GPT4}:</b> {count_income_transactions[ServiceType.GPT4]}
    - <b>{ServiceType.DALLE3}:</b> {count_income_transactions[ServiceType.DALLE3]}
    - <b>{ServiceType.FACE_SWAP}:</b> {count_income_transactions[ServiceType.FACE_SWAP]}
    - <b>{ServiceType.ADDITIONAL_CHATS}:</b> {count_income_transactions[ServiceType.ADDITIONAL_CHATS]}
    - <b>{ServiceType.ACCESS_TO_CATALOG}:</b> {count_income_transactions[ServiceType.ACCESS_TO_CATALOG]}
    - <b>{ServiceType.VOICE_MESSAGES}:</b> {count_income_transactions[ServiceType.VOICE_MESSAGES]}
    - <b>{ServiceType.FAST_MESSAGES}:</b> {count_income_transactions[ServiceType.FAST_MESSAGES]}
    - <b>{ServiceType.STANDARD}:</b> {count_income_transactions[ServiceType.STANDARD]}
    - <b>{ServiceType.VIP}:</b> {count_income_transactions[ServiceType.VIP]}
    - <b>{ServiceType.PLATINUM}:</b> {count_income_transactions[ServiceType.PLATINUM]}

    - <b>Всего:</b> {count_transactions_total}
<span class="tg-spoiler">
2️⃣ <b>Расходы:</b>
   - <b>{ServiceType.GPT3}:</b> {round(count_expense_money[ServiceType.GPT3], 2)}$
   - <b>{ServiceType.GPT4}:</b> {round(count_expense_money[ServiceType.GPT4], 2)}$
   - <b>{ServiceType.DALLE3}:</b> {round(count_expense_money[ServiceType.DALLE3], 2)}$
   - <b>{ServiceType.FACE_SWAP}:</b> {round(count_expense_money[ServiceType.FACE_SWAP], 2)}$
   - <b>{ServiceType.VOICE_MESSAGES}:</b> {round(count_expense_money[ServiceType.VOICE_MESSAGES], 2)}$
   - <b>{ServiceType.SERVER}:</b> {round(count_expense_money[ServiceType.SERVER])}$
   - <b>{ServiceType.DATABASE}:</b> {round(count_expense_money[ServiceType.DATABASE])}

   - <b>Всего:</b> {round(count_expense_total_money, 2)}$
3️⃣ <b>Доходы:</b>
    💳 <b>Подписки:</b> {count_income_subscriptions_total_money}₽
    - <b>{ServiceType.STANDARD} {emojis[ServiceType.STANDARD]}:</b> {count_income_money[ServiceType.STANDARD]}₽
    - <b>{ServiceType.VIP} {emojis[ServiceType.VIP]}:</b> {count_income_money[ServiceType.VIP]}₽
    - <b>{ServiceType.PLATINUM} {emojis[ServiceType.PLATINUM]}:</b> {count_income_money[ServiceType.PLATINUM]}₽

    💵 <b>Пакеты:</b> {count_income_packages_total_money}₽
    - <b>{ServiceType.GPT3}:</b> {count_income_money[ServiceType.GPT3]}₽
    - <b>{ServiceType.GPT4}:</b> {count_income_money[ServiceType.GPT4]}₽
    - <b>{ServiceType.DALLE3}:</b> {count_income_money[ServiceType.DALLE3]}₽
    - <b>{ServiceType.FACE_SWAP}:</b> {count_income_money[ServiceType.FACE_SWAP]}₽
    - <b>{ServiceType.ADDITIONAL_CHATS}:</b> {count_income_money[ServiceType.ADDITIONAL_CHATS]}₽
    - <b>{ServiceType.ACCESS_TO_CATALOG}:</b> {count_income_money[ServiceType.ACCESS_TO_CATALOG]}₽
    - <b>{ServiceType.VOICE_MESSAGES}:</b> {count_income_money[ServiceType.VOICE_MESSAGES]}₽
    - <b>{ServiceType.FAST_MESSAGES}:</b> {count_income_money[ServiceType.FAST_MESSAGES]}₽

    - <b>Всего:</b> {count_income_total_money}₽
4️⃣ <b>Вал:</b> {round(count_total_money, 2)}₽
</span>
💬 <b>Созданные чаты</b>
{chat_info}

    - <b>Всего:</b> {count_chats_usage['ALL']}
🎭 <b>Выбранные Face Swap</b>
{face_swap_info}

    - <b>Всего:</b> {count_face_swap_usage['ALL']}

🔍 Это всё, что тебе нужно знать о текущем положении дел. Вперёд, к новым достижениям! 🚀
"""

    @staticmethod
    def catalog_manage_create_role_confirmation(
        role_system_name: str,
        role_names: Dict,
        role_descriptions: Dict,
        role_instructions: Dict,
    ):
        names = ""
        for i, (language_code, name) in enumerate(role_names.items()):
            names += f'{language_code}: {name}'
            names += '\n' if i < len(role_names.items()) - 1 else ''
        descriptions = ""
        for i, (language_code, description) in enumerate(role_descriptions.items()):
            descriptions += f'{language_code}: {description}'
            descriptions += '\n' if i < len(role_descriptions.items()) - 1 else ''
        instructions = ""
        for i, (language_code, instruction) in enumerate(role_instructions.items()):
            instructions += f'{language_code}: {instruction}'
            instructions += '\n' if i < len(role_instructions.items()) - 1 else ''

        return f"""
🌟 Вот что вы создали: 🎩

🤖 Системное название:
{role_system_name}

🌍 Имена:
{names}

💬 Описания:
{descriptions}

📜 Инструкции:
{instructions}

🔍 Перед вами полная картина вашего нового помощника. Если все выглядит идеально, нажмите "Подтвердить" и отправьте его на завоевание AI-мира! Нужны правки? Без проблем, выберите "Отменить" и начните всё сначала. Ваше творение ждет своего часа! 🌟
"""

    @staticmethod
    def catalog_manage_role_edit(
        role_system_name: str,
        role_names: Dict,
        role_descriptions: Dict,
        role_instructions: Dict,
    ):
        names = ""
        for i, (language_code, name) in enumerate(role_names.items()):
            names += f'{language_code}: {name}'
            names += '\n' if i < len(role_names.items()) - 1 else ''
        descriptions = ""
        for i, (language_code, description) in enumerate(role_descriptions.items()):
            descriptions += f'{language_code}: {description}'
            descriptions += '\n' if i < len(role_descriptions.items()) - 1 else ''
        instructions = ""
        for i, (language_code, instruction) in enumerate(role_instructions.items()):
            instructions += f'{language_code}: {instruction}'
            instructions += '\n' if i < len(role_instructions.items()) - 1 else ''

        return f"""
🎨 Настройка роли 🖌️

🔧 Вы решили отполировать {role_system_name}! Настало время превратить его в настоящую звезду AI-мира 🌟

🌍 Имена:
{names}

💬 Описания:
{descriptions}

📜 Инструкции:
{instructions}

🛠️ Теперь ваша очередь внести магию! Выберите, что хотите изменить:
- "Изменить имя" 📝
- "Изменить описание" 📖
- "Изменить инструкцию" 🗒️
- "Назад" 🔙
"""

    @staticmethod
    def face_swap_manage_create_package_confirmation(
        package_system_name: str,
        package_names: Dict,
    ):
        names = ""
        for i, (language_code, name) in enumerate(package_names.items()):
            names += f'{language_code}: {name}'
            names += '\n' if i < len(package_names.items()) - 1 else ''

        return f"""
🌟 <b>Вот и всё! Ваш новый пакет FaceSwap почти готов к дебюту!</b> 🎉

📝 Проверьте все детали:
- 🤖 Системное название:
{package_system_name}

- 🌍 Имена:
{names}

🔍 Убедитесь, что все верно. Это ваше творение, и оно должно быть идеальным!

👇 Выберите действие
"""

    @staticmethod
    def profile(subscription_type: SubscriptionType,
                gender: UserGender,
                current_model: str,
                monthly_limits,
                additional_usage_quota) -> str:
        raise NotImplementedError

    # Subscription
    @staticmethod
    def subscribe(currency: Currency) -> str:
        raise NotImplementedError

    @staticmethod
    def choose_how_many_months_to_subscribe(subscription_type: SubscriptionType) -> str:
        raise NotImplementedError

    @staticmethod
    def cycles_subscribe() -> str:
        raise NotImplementedError

    @staticmethod
    def confirmation_subscribe(subscription_type: SubscriptionType, subscription_period: SubscriptionPeriod) -> str:
        raise NotImplementedError

    # Package
    @staticmethod
    def buy() -> str:
        raise NotImplementedError

    @staticmethod
    def choose_min(package_type: PackageType) -> str:
        raise NotImplementedError

    # Chats
    @staticmethod
    def chats(current_chat_name: str, total_chats: int, available_to_create_chats: int) -> str:
        raise NotImplementedError

    # Face swap
    @staticmethod
    def choose_face_swap_package(name: str, available_images: int, total_images: int, used_images: int) -> str:
        raise NotImplementedError

    @staticmethod
    def face_swap_package_forbidden(available_images: int) -> str:
        raise NotImplementedError

    @staticmethod
    def wait_for_another_request(seconds: int) -> str:
        raise NotImplementedError

    @staticmethod
    def processing_request_text() -> str:
        raise NotImplementedError

    @staticmethod
    def processing_request_image() -> str:
        raise NotImplementedError

    @staticmethod
    def processing_request_face_swap() -> str:
        raise NotImplementedError
