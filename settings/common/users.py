import os
from flask import current_app
from settings.models import db
from settings.config import db_path

USER_DB_URI = 'sqlite:///' + os.path.join(db_path, 'user_{}.db')

#
# def get_user_settings():
#     todo: this function should query the db to check authorization and get settings (like db uri)
#
#     return db_url, settings


def prepare_bind(user_id):
    if user_id not in current_app.config['SQLALCHEMY_BINDS']:
        current_app.config['SQLALCHEMY_BINDS'][user_id] = USER_DB_URI.format(user_id)
        if user_id == 5: current_app.config['SQLALCHEMY_BINDS'][user_id] = os.environ['AMAZON_RDS_DB_URL']
        # todo  create model and db here
        #       create model from template, use model to db.create_all[, delete model]
    return current_app.config['SQLALCHEMY_BINDS'][user_id]


def get_user_session(user_id):
    # if user_id not in get_known_tenants():
    #     return None
    prepare_bind(user_id)
    engine = db.get_engine(current_app, bind=user_id)
    session_maker = db.sessionmaker()
    session_maker.configure(bind=engine)
    session = session_maker()
    return session
