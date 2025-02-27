from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    name = Column(String(50), primary_key=True, nullable=False)
    password = Column(String(50), nullable=False)

