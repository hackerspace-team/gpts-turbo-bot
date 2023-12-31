from datetime import datetime, timezone

from bot.database.models.common import Currency


class TransactionType:
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"


class ServiceType:
    STANDARD = "STANDARD"
    VIP = "VIP"
    PLATINUM = "PLATINUM"
    GPT3 = "GPT3"
    GPT4 = "GPT4"
    DALLE3 = "DALLE3"
    FACE_SWAP = "FACE_SWAP"
    ADDITIONAL_CHATS = "ADDITIONAL_CHATS"
    FAST_MESSAGES = "FAST_MESSAGES"
    VOICE_MESSAGES = "VOICE_MESSAGES"
    ACCESS_TO_CATALOG = "ACCESS_TO_CATALOG"
    OTHER = "OTHER"


class Transaction:
    id: str
    user_id: str
    type: TransactionType
    service: ServiceType
    amount: float
    currency: Currency
    quantity: int
    created_at: datetime
    edited_at: datetime

    def __init__(self,
                 id: str,
                 user_id: str,
                 type: TransactionType,
                 service: ServiceType,
                 amount: float,
                 currency: Currency,
                 quantity=1,
                 created_at=None,
                 edited_at=None):
        self.id = str(id)
        self.user_id = str(user_id)
        self.type = type
        self.service = service
        self.amount = amount
        self.currency = currency
        self.quantity = quantity

        current_time = datetime.now(timezone.utc)
        self.created_at = created_at if created_at is not None else current_time
        self.edited_at = edited_at if edited_at is not None else current_time

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "type": self.type,
            "service": self.service,
            "amount": self.amount,
            "currency": self.currency,
            "quantity": self.quantity,
            "created_at": self.created_at,
            "edited_at": self.edited_at
        }