from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_filename = "deathco.db"

engine = create_engine(f"sqlite:///{db_filename}", echo=True)
Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback
        raise
    finally:
        session.close()


class Base(object):
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


def init_db():
    import models

    Base.metadata.create_all(bind=engine)
