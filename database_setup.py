from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Title(Base):
    __tablename__ = 'titles'
    id = Column(Integer, primary_key=True)
    name = Column(String(500), unique=True)


engine = create_engine('sqlite:///test.db')


Base.metadata.create_all(engine)