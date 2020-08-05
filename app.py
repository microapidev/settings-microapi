from flask import render_template, url_for
from settings.config import connex_app

connex_app.add_api('swagger.yaml', options={"swagger_url": '/ui'})
application = connex_app.app


@connex_app.route('/')
def redir():
    swagger_doc_url = 'v1/ui'
    return render_template('404.html', url_for=url_for, doc=swagger_doc_url)


if __name__ == '__main__':
    application.run(debug=True, port=5207)
