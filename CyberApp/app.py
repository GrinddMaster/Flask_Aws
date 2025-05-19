from flask import Flask


def Create_app():
    app = Flask(__name__)
    app.secret_key = " Test key"
    from CyberApp.blueprints.Login.routes import login
    from CyberApp.blueprints.Core.routes import core
    from CyberApp.blueprints.Create_User.routes import signup
    app.register_blueprint(login, url_prefix='/')
    app.register_blueprint(signup, url_prefix='/')
    app.register_blueprint(core)

    return app
