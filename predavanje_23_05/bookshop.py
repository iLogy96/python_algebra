from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    books = relationship("Book", backref="author")

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"Author {self.name}, {self.surname}"


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey("author.id"))

    def __init__(self, title, author_id):
        self.title = title
        self.author_id = author_id

    def __repr__(self):
        return f"Book: {self.title}, by {self.author}"


# Setup database
engine = create_engine("sqlite:///predavanje_23_05/bookshop.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# Data
authors = [
    ("John", "Doe"),
    ("Jane", "Doe"),
    ("Anna", "Blue"),
    ("John", "Williams"),
    ("Random", "Guy"),
    ("Smth", "Smth"),
]
books = [
    ("title 1", 1),
    ("title 2", 2),
    ("title 3", 3),
    ("title 4", 4),
    ("title 5", 5),
    ("title 6", 6),
]

# Add authors to the database
for name, surname in authors:
    new_author = Author(name=name, surname=surname)
    session.add(new_author)
session.commit()

# Add books to the database
for title, author_id in books:
    new_book = Book(title=title, author_id=author_id)
    session.add(new_book)
session.commit()
