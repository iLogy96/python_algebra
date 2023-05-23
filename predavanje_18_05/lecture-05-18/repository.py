import sqlalchemy as db

from model import Author, Book, Publisher, Base


def add_book(session, author_name, book_title, publisher_name):
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
    author.publishers.append(publisher)
    session.add(book)
    session.commit()
    return True


"""
SELECT *,
    COUNT(*) AS total_books
FROM Book
JOIN Book_Publisher ON 
    Book.id==Book_Publisher.book_id 
    AND Publisher.id==Book_Publisher.publisher
JOIN Publisher ON ....
GROUP BY Publisher

20 knjiga od 3 izdavača

ali želimo samo 3 retka
# Penguin Random House, 6 knjiga
# Parrot Random House, 6 knjiga
# Random House, 2 knjiga
"""
def get_books_by_publisher(session):
    return (session.query(
        Publisher.name,
        #    COUNT(*) AS total_books
        db.func.count(Book.title).label("total_books")
    )
    .join(Publisher.books)
    .group_by(Publisher.id)
    )


"""
dohvaćamo ukupan broj autora po izdavaču, 
sortirano po broju autora
"""
def get_authors_by_publisher(session, ascending=True):
    sort = db.asc if ascending else db.desc # ORDER BY ASC ili DESC

    return (session.query(
        Publisher.name,
        db.func.count(Author.name).label("total_authors")
    )
    .join(Publisher.authors)
    .group_by(Publisher.id)
    .order_by(sort("total_authors"))
    )


def books_by_author(text):
# funkcija vraća informacije o autoru, uz 
# dodatak - ukupan broj knjiga u bazi po autoru
    pass

def search_name(text):
# funkcija provjerava sadrži li naslov 
# u bazi string argument
# (LIKE iz SQL-a)
    pass
