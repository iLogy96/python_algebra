import sqlalchemy as db

from sqlalchemy.orm import sessionmaker

from model import Author, Book, Publisher, Base
from repository import *


def main():
    db_engine = db.create_engine("sqlite:///lecture-05-15/book_shop.db")
    Base.metadata.create_all(db_engine)

    Session = sessionmaker()
    Session.configure(bind=db_engine)
    session = Session()

    

if __name__ == "__main__":
    main()
    