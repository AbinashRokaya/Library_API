from fastapi import Depends,status,HTTPException
from sqlalchemy.orm import Session
from typing import List
from model.book import BookAuthor
from schema.book_author_schema import Book_AuthorOut,Book_AuthorCreate


def create_book_author(author_book:Book_AuthorCreate,db:Session)->Book_AuthorOut:
   authorbooks=BookAuthor(book_id=author_book.book_id,author_id=author_book.author_id)
   db.add(authorbooks)
   db.commit()
   db.refresh(authorbooks)

   new_author_books=Book_AuthorOut(book_id=authorbooks.book_id,author_id=authorbooks.author_id)
   return new_author_books
