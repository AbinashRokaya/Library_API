from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from typing import Annotated,List
from fastapi import Depends

URL_DATABASE="postgresql://postgres:abinash@localhost:5432/Library"

engine=create_engine(URL_DATABASE)
sessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

