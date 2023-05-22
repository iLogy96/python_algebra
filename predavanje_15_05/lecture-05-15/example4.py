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


def add_book(session, book_title, author_name, publisher_name):
    name, surname = author_name.split()
    
    # postoji li već točno ova kniga u bazi
    # sa točno tim autorom i točno tim izdavačem
    book = (session.query(Book)
        .filter(Book.title == book_title)
        .filter(
            db.and_(
                Author.name == name, Author.surname == surname
            )
        )
        .filter(Book.publishers.any(Publisher.name == publisher_name))
    ).one_or_none()

    if (book is not None):
        return False

    book = Book(title=book_title)

    author = (session.query(Author)
        .filter(
            db.and_(
                Author.name == name, Author.surname == surname
            )
        )
    ).one_or_none()
    
    # ako autora nema u bazi, kreirajmo ga
    if (author is None):
        author = Author(name=name, surname=surname)

    publisher = (session.query(Publisher)
        .filter(Publisher.name==publisher_name)
        .one_or_none()
    )

    # ako izdavač već nije u bazi, kreirajmo ga
    if (publisher is None):
        publisher = Publisher(name=publisher_name)

    session.add(author)
    session.add(publisher)

    book.Author=author
    book.publishers.append(publisher)

    session.add(book)
    session.commit()
    return True


def main():
    db_engine = db.create_engine("sqlite:///lecture-05-15/book_shop.db")
    Base.metadata.create_all(db_engine)

    Session = sessionmaker()
    Session.configure(bind=db_engine)
    session = Session()

    book = ["Foundation", "Isaac Asimov", "Parrot Random House"]
    # result = add_book(session, book[0], book[1], book[2])
    if not add_book(session, book[0], book[1], book[2]):
        print("Knjiga već postoji!")
    else:
        print("Knjiga dodana u bazu!")


if __name__ == "__main__":
    main()
    