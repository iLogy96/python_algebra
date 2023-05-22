import sqlalchemy as db

from model import Author, Book, Publisher, Base


def add_book(session, author_name, book_title, publisher_name):
    name, surname = author_name.split()
    book = (
        session.query(Book)
        .filter(Book.title == book_title)
        .filter(db.and_(Author.name == name, Author.surname == surname))
        .filter(Book.publishers.any(Publisher.name == publisher_name))
    ).one_or_none()

    if book is not None:
        return False

    book = Book(title=book_title)

    author = (
        session.query(Author).filter(
            db.and_(Author.name == name, Author.surname == surname)
        )
    ).one_or_none()

    # ako autora nema u bazi, kreirajmo ga
    if author is None:
        author = Author(name=name, surname=surname)

    publisher = (
        session.query(Publisher).filter(Publisher.name == publisher_name).one_or_none()
    )

    # ako izdavač već nije u bazi, kreirajmo ga
    if publisher is None:
        publisher = Publisher(name=publisher_name)

    session.add(author)
    session.add(publisher)

    book.Author = author
    book.publishers.append(publisher)
    author.publishers.append(publisher)
    session.add(book)
    session.commit()
    return True


def get_books_by_publisher(session):
    return (
        session.query(
            Publisher.name,
            #    COUNT(*) AS total_books
            db.func.count(Book.title).label("total_books"),
        )
        .join(Publisher.books)
        .group_by(Publisher.id)
    )


def get_authors_by_publisher(session, ascending=True):
    sort = db.asc if ascending else db.desc  # ORDER BY ASC ili DESC

    return (
        session.query(Publisher.name, db.func.count(Author.name).label("total_authors"))
        .join(Publisher.authors)
        .group_by(Publisher.id)
        .order_by(sort("total_authors"))
    )


def books_by_author(session, text):
    # funkcija vraća informacije o autoru, uz
    # dodatak - ukupan broj knjiga u bazi po autoru
    author_name = text.strip()
    name, surname = author_name.split()

    author = (
        session.query(Author)
        .filter(Author.name == name, Author.surname == surname)
        .one_or_none()
    )

    if author is not None:
        total_books = (
            session.query(db.func.count(Book.id))
            .filter(Book.author_id == author.id)
            .scalar()
        )
        return f"Author: {author_name}\nTotal books: {total_books}"
    else:
        return f"No information found for author: {author_name}"


def search_name(session, text):
    # funkcija provjerava sadrži li naslov
    # u bazi string argument
    # (LIKE iz SQL-a)
    book_title = f"%{text.strip()}%"

    books = session.query(Book).filter(Book.title.ilike(book_title)).all()

    if books:
        print("Books found:")
        for book in books:
            return f"- {book.title}"
    else:
        return "No books found."
