from sqlalchemy import create_engine, Column, Integer, String,Numeric,Enum,ForeignKey,DateTime
from schema.enum import ActionType
from database.database import Base


class Transactionlogs(Base):
    __tablename__="trans"

    transaction_id=Column(Integer,primary_key=True,index=True)
    book_id=Column(Integer,ForeignKey("book.book_id",ondelete="CASCADE"))
    stud_id=Column(Integer,ForeignKey("student.stud_id",ondelete="CASCADE"))
    action =Column(Enum(ActionType),default=ActionType.borrow)
    transaction_date=Column(DateTime)
    staff_id=Column(Integer,ForeignKey("staff.staff_id",ondelete="CASCADE"))
    