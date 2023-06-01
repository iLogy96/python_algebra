from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Index, UniqueConstraint

engine = create_engine("sqlite:///SmartKey/smartkey.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    pin = Column(String, unique=True)
    active = Column(Boolean)

    __table_args__ = (
        Index("idx_users_name", name),
        UniqueConstraint("name", name="uq_users_name"),
        UniqueConstraint("pin", name="uq_users_pin")
    )


Base.metadata.create_all(engine)

# Popunjavanje baze s korisnicima
def populate_users():
    users = [
        {"name": "John Doe", "pin": "1234", "active": True},
        {"name": "Jane Smith", "pin": "5678", "active": True},
        {"name": "Admin", "pin": "0000", "active": True}
    ]

    for user_data in users:
        user = User(**user_data)
        session.add(user)

    session.commit()

# Poziv funkcije za popunjavanje korisnika
populate_users()
