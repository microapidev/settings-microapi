from flask import render_template, url_for
from settings.config import connex_app
from settings.models import db

connex_app.add_api('swagger.yaml', options={"swagger_url": '/doc'})
application = connex_app.app
db.create_all()


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
