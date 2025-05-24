from fastapi import APIRouter,Depends,HTTPException,status

from schema.book_shema import BookCreate,BookOut,BookCreate_1,BookCreateResponse

from typing import List
from auth.auth_dependancy import get_current_user
from schema.token_shema import SystemUser
from repo import book_repo
from repo import book_category_repo
from repo import publisher_repo
from repo import author_repo
from repo import book_author_repo
from database.database import get_db
from sqlalchemy.orm import Session
from schema.book_Category import BookCategoryCreate
from schema.publisher import PublisherCreate
from schema.author_schema import AuthorCreate
from schema.book_author_schema import Book_AuthorCreate,Book_AuthorOut

route=APIRouter(
    prefix="/book",
    tags=['Book']

)



@route.post("/add")
def bookCreate(book:BookCreate,db: Session = Depends(get_db),current_user:SystemUser=Depends(get_current_user))->BookCreateResponse:
    book_category=book_category_repo.create_category(book.category,db=db)
    publisher=publisher_repo.create_publisher(book.publisher,db)
    author=author_repo.create_author(book.author,db=db)

    book_detail=BookCreate_1(description=book.description,
                             category_id=book_category.category_id,
                             publisher_id=publisher.publisher_id,
                             )
    book_description=book_repo.create_book(book_detail,db=db)
    book_auhtor_detail=Book_AuthorCreate(book_id=book_description.book_id,author_id=author.author_id)
    book_Author=book_author_repo.create_book_author(book_auhtor_detail,db=db)
    response=BookCreateResponse(description=book_description.dict(),category=BookCategoryCreate(category_name=book_category.category_name),
                                publisher=PublisherCreate(publisher_name=publisher.publisher_name),
                                author=AuthorCreate(author_name=author.author_name))

    return response

    
    

# @route.get("/all",response_model=List[BookOut],)
# def get_all_book(db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
#     all_books=db.query(Book).all()
#     if not all_books:
#         raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail="Book not found")
    
#     return all_books


# @route.get("/{book_id}",response_model=BookOut)
# def get_book_id(book_id:int,db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
#     book_id_detail=db.query(Book).filter(Book.book_id==book_id).first()
#     if not book_id_detail:
#         raise HTTPException(status_code=201,detail=f"Book id {book_id} not found")
    
#     return book_id_detail

