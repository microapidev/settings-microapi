import os
import secrets
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

base_dir = os.path.dirname(__file__)
db_path = base_dir  # os.path.join(base_dir, 'database')

DASHBOARD_DB_URI = 'sqlite:///' + os.path.join(db_path, 'dashboard.db')
USER_DB_URI = 'sqlite:///' + os.path.join(db_path, 'settings.db')

sqlalchemy_binds = {'dashboard': DASHBOARD_DB_URI}
connex_app = connexion.App(__name__, specification_dir=base_dir)
app = connex_app.app

app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = USER_DB_URI
app.config['SQLALCHEMY_BINDS'] = sqlalchemy_binds
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
tokens = {}
