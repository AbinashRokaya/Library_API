from sqlalchemy import create_engine, Column, Integer, String,Numeric,Enum,ForeignKey,DateTime,func
from schema.enum import Status
from database.database import Base



class Book(Base):
    __tablename__="book"

    book_id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    edition=Column(String)
    cost=Column(Numeric(10,2))
    copies=Column(Integer)
    status = Column(Enum(Status), default=Status.available, nullable=False)
    category_id=Column(Integer,ForeignKey("book_category.category_id",ondelete="CASCADE"))
    publisher_id=Column(Integer,ForeignKey("publisher.publisher_id",ondelete="CASCADE"))


class BookCategory(Base):
    __tablename__="book_category"

    category_id=Column(Integer,primary_key=True,index=True)
    category_name=Column(String,unique=True)




class Publisher(Base):
    __tablename__="publisher"

    publisher_id=Column(Integer,primary_key=True,index=True)
    publisher_name=Column(String)


class Author(Base):
    __tablename__="author"


    author_id=Column(Integer,primary_key=True,index=True)
    author_name=Column(String)

class BookAuthor(Base):
    __tablename__="bookauthor"

  
    book_id=Column(Integer,ForeignKey("book.book_id",ondelete="CASCADE"),primary_key=True)
    author_id=Column(Integer,ForeignKey("author.author_id",ondelete="CASCADE"),primary_key=True)

class BookBorrowers(Base):
    __tablename__="borrowers"

    borrowers_id =Column(Integer,primary_key=True,index=True)
    book_id=Column(Integer,ForeignKey("book.book_id",ondelete="CASCADE"))
    stud_id=Column(Integer,ForeignKey("student.stud_id",ondelete="CASCADE"))
    release_date=Column(DateTime,server_default=func.now())
    due_date=Column(DateTime)


class BookReturns(Base):
    __tablename__="returns"

    return_id=Column(Integer,primary_key="True",index=True)
    borrowers_id=Column(Integer,ForeignKey("borrowers.borrowers_id",ondelete="CASCADE"))
    return_date=Column(DateTime)
    fine_amount=Column(Numeric(10,2))