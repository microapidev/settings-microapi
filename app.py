from settings.config import connex_app
from flask import redirect

connex_app.add_api ('swagger.yaml', arguments={'swagger_url': 'doc'})
application = connex_app.app


@connex_app.route('/')
def redir():
    return redirect('/v1/ui', 302)


if __name__ == '__main__':
    application.run(debug=True, port=5207)
