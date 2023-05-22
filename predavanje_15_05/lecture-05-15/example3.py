import sqlalchemy as db

from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# autor-knjiga-izdavač

"""
CREATE TABLE Author(
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    surname VARCHAR
);
"""

author_publisher = db.Table(
    "Author_Publisher",
    Base.metadata,
    db.Column("author_id", db.Integer, db.ForeignKey("Author.id")),
    db.Column("publisher_id", db.Integer, db.ForeignKey("Publisher.id"))
)

book_publisher = db.Table(
    "Book_Publisher",
    Base.metadata,
    db.Column("book_id", db.Integer, db.ForeignKey("Book.id")),
    db.Column("publisher_id", db.Integer, db.ForeignKey("Publisher.id")),
)


class Author(Base):
    __tablename__ = "Author"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    books = relationship("Book", backref=backref("Author"))
    publishers = relationship(
        "Publisher", secondary=author_publisher, back_populates="authors")

class Book(Base):
    __tablename__ = "Book"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey("Author.id"))
    publishers = relationship(
        "Publisher", secondary=book_publisher, back_populates="books")

class Publisher(Base):
    __tablename__ = "Publisher"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    authors = relationship(
        "Author", secondary=author_publisher, back_populates="publishers")
    books = relationship(
        "Book", secondary=book_publisher, back_populates="publishers")


db_engine = db.create_engine("sqlite:///lecture-05-15/book_shop.db")
Base.metadata.create_all(db_engine)

Session = sessionmaker()
Session.configure(bind=db_engine)
session = Session()

author = Author(name="Stephen", surname="King")
book = Book(title="The Shining")
publisher = Publisher(name="Penguin Random House")

book.Author=author
book.publishers.append(publisher)

session.add(book)
session.add(author)
session.add(publisher)

session.commit()
