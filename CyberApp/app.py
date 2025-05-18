from flask import Flask


def Create_app():
    app = Flask(__name__)
    from CyberApp.blueprints.Login.routes import login
    from CyberApp.blueprints.Core.routes import core
    app.register_blueprint(login, url_prefix='/')
    app.register_blueprint(core)

    return app
