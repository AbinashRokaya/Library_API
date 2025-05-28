from fastapi import FastAPI
import uvicorn
from database.database import engine,sessionLocal,Base
import model
from routes import (book_author_route,Book_route,book_borrowers_routes,book_return_route,
                    book_category_route,staff_routes,student_routes,transactionlogs_routes,publisher_route,author_route)
from auth import login

app=FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(Book_route.route)
app.include_router(book_category_route.route)
app.include_router(book_borrowers_routes.route)
app.include_router(book_return_route.route)
app.include_router(book_author_route.route)
app.include_router(transactionlogs_routes.route)
app.include_router(staff_routes.route)
app.include_router(student_routes.route)
app.include_router(publisher_route.route)
app.include_router(author_route.route)
app.include_router(login.route)


@app.get("/")
def index():
    return {"Surver is running"}


if __name__=="__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True,loop="asyncio")

