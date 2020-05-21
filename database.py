from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import Model
from contextlib import contextmanager

db_filename = "deathco.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_filename}"

db = SQLAlchemy(app)


@contextmanager
def session_scope():
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
