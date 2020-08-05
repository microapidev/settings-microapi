import os
from flask import current_app
from sqlalchemy import MetaData
from settings.models import db, user_table
from settings.config import db_path

USER_DB_URI = 'sqlite:///' + os.path.join(db_path, 'user_{}.db')


# def get_user_settings():
#     todo: this function should query the db to check authorization and get settings (like db uri)
#
#     return db_url, settings


def prepare_bind(user_id):
    if user_id not in current_app.config['SQLALCHEMY_BINDS']:
        current_app.config['SQLALCHEMY_BINDS'][user_id] = USER_DB_URI.format(user_id)
        if user_id == '5':
            current_app.config['SQLALCHEMY_BINDS'][user_id] = os.environ['AMAZON_RDS_DB_URL']
    return current_app.config['SQLALCHEMY_BINDS'][user_id]


def create_db_tables_if_absent(engine):
    metadata = MetaData()
    table = user_table(metadata)
    metadata.create_all(engine, tables=[table])


def get_user_session(user_id):
    prepare_bind(user_id)
    engine = db.get_engine(current_app, bind=user_id)
    create_db_tables_if_absent(engine)
    session_maker = db.sessionmaker()
    session_maker.configure(bind=engine)
    session = session_maker()
    return session
