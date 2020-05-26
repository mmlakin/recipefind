# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from contextlib import contextmanager

app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)


@contextmanager
def db_session_scope():
    session = db.session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def init_db():
    import models

    db.create_all()
