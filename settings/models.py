from datetime import datetime
from settings.config import db, ma
from sqlalchemy import Column, Table, String, DateTime


class Config(db.Model):
    __tablename__ = 'configurations'
    config_tag = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, nullable=False)
    api_name = db.Column(db.String(), nullable=False)
    current_config = db.Column(db.String(), nullable=False)
    previous_config = db.Column(db.String(), nullable=True)
    default_config = db.Column(db.String(), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "Config <{id}: {api_name}>".format(id=self.id, api_name=self.api_name)

    __str__ = __repr__


def user_table(metadata):
    config_table = Table('configurations', metadata,
                         Column('config_tag', String, primary_key=True),
                         Column('user_id', String, nullable=False),
                         Column('api_name', String, nullable=False),
                         Column('current_config', String, nullable=False),
                         Column('previous_config', String, nullable=True),
                         Column('default_config', String, nullable=True),
                         Column('created_at', DateTime, default=datetime.utcnow),
                         Column('updated_at', DateTime, default=datetime.utcnow),
                         )
    return config_table


class Dashboard(db.Model):
    __tablename__ = 'dashboard_settings'
    __bind_key__ = 'dashboard'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, nullable=False)
    current_config = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __str__(self):
        return "Dashboard <{id}: {api_name}>".format(id=self.id, api_name=self.api_name)

    __repr__ = __str__


class ConfigSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Config
        sqla_session = db.session


class DashSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Dashboard
        sqla_session = db.session


config_schema = ConfigSchema()
config_schema_many = ConfigSchema(many=True)
