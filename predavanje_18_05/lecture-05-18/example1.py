import sqlalchemy as db

from sqlalchemy.orm import sessionmaker

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


def main():
    db_engine = db.create_engine("sqlite:///lecture-05-15/book_shop.db")
    Base.metadata.create_all(db_engine)

    Session = sessionmaker()
    Session.configure(bind=db_engine)
    session = Session()

    books = [
        ["Isaac Asimov","Foundation","Random House"],
        ["Pearl Buck","The Good Earth","Random House"],
        ["Pearl Buck","The Good Earth","Simon & Schuster"],
        ["Tom Clancy","The Hunt For Red October","Berkley"],
        ["Tom Clancy","Patriot Games","Simon & Schuster"],
        ["Stephen King","It","Random House"],
        ["Stephen King","It","Penguin Random House"],
        ["Stephen King","Dead Zone","Random House"],
        ["Stephen King","The Shining","Penguin Random House"],
        ["John Carre","Tinker, Tailor, Soldier, Spy: A George Smiley Novel","Berkley"],
        ["Alex Michaelides","The Silent Patient","Simon & Schuster"],
        ["Carol Shaben","Into The Abyss","Simon & Schuster"]
    ]

    for book in books:
        if not add_book(session, book[0], book[1], book[2]):
            # print("Knjiga već postoji!")
            pass
        else:
            print("Knjiga dodana u bazu!")

    # dohvatiti listu izdavača sa brojem izdanih knjiga
    # Penguin Random House, 6 knjiga
    # Parrot Random House, 6 knjiga
    # Random House, 2 knjiga
    
    publishers_books = get_books_by_publisher(session)
    for publisher in publishers_books:
        print(f"Izdavač: {publisher[0]}, ukupno knjiga: {publisher[1]}")
    
    publishers_authors = get_authors_by_publisher(session, False)
    for publisher in publishers_authors:
        print(f"Izdavač: {publisher[0]}, ukupno autora: {publisher[1]}")


if __name__ == "__main__":
    main()
    