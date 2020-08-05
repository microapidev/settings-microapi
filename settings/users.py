from flask import current_app
from sqlalchemy import MetaData
from settings.models import db, user_table
from settings.common.helpers import get_db_url


def prepare_bind(user_id):
    if user_id not in current_app.config['SQLALCHEMY_BINDS']:
        current_app.config['SQLALCHEMY_BINDS'][user_id] = get_db_url(user_id)
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
