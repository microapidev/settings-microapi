from settings.config import connex_app, db_path
from flask import render_template, url_for
import os

connex_app.add_api('swagger.yaml', options={"swagger_url": '/doc'})
application = connex_app.app


@connex_app.route('/')
def redir():
    swagger_doc_url = 'v1/doc'
    return render_template('404.html', url_for=url_for, doc=swagger_doc_url)


# if os.environ['FLASK_ENV'] == 'development' and not os.path.exists(os.path.join(db_path, 'settings.db')):
#     from settings.models import db
#     db.create_all()
#     db.session.commit()


if __name__ == '__main__':
    application.run(debug=True, port=5207)
