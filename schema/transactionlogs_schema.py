from pydantic import BaseModel
from datetime import datetime
from schema.enum import ActionType


class TransactionLogBase(BaseModel):
    book_ID: int
    stud_ID: int
    action: ActionType
    transaction_date: datetime
    staff_ID: int
    fine_amount: float


class TransactionLogCreate(TransactionLogBase):
    pass


class TransactionLogResponse(TransactionLogBase):
    transaction_id: int

    class Config:
        orm_mode = True

