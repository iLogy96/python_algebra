from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


# Kreiranje klase za bazu
class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return (
            f"({self.ssn}) {self.firstname} {self.lastname}, ({self.gender},{self.age})"
        )


class Thing(Base):
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f"({self.tid}) {self.description} owned by {self.owner}"


# Osnovni podaci za pokretanje i kreiranje baze
engine = create_engine("sqlite:///vjezba_SQL/mydb.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
# Setup i addanje u bazu
# p1 = Person(12312, "Mike", "Smith", "m", 35)
# p2 = Person(12322, "Bob", "Blue", "m", 24)
# p3 = Person(13232, "Hannah", "Blue", "f", 66)

# session.add(p1)
# session.add(p2)
# session.add(p3)
# session.commit()

# t1 = Thing(1, "Car", p1.ssn)
# t2 = Thing(2, "PS5", p1.ssn)
# t3 = Thing(3, "Tool", p2.ssn)
# t4 = Thing(4, "Book", p3.ssn)
# session.add(t1)
# session.add(t2)
# session.add(t3)
# session.add(t4)
# session.commit()

results = (
    session.query(Thing, Person)
    .filter(Thing.owner == Person.ssn)
    .filter(Person.firstname == "Hannah")
)
for r in results:
    print(r)
