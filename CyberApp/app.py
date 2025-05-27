from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import urllib.parse

db = SQLAlchemy()
username = '-'
password = '-'
host = '127.0.0.1'
port = '3306'
database_name = 'Cyber_Proj'

encoded_password = urllib.parse.quote_plus(password)


def create_app():
    app = Flask(__name__)
    app.secret_key = " Test key"
    app.config['SQLALCHEMY_DATABASE_URI'] = (
     f'mysql+pymysql://{username}:{encoded_password}'
     f'@{host}:{port}/{database_name}'
        )
    db.init_app(app)

    from CyberApp.blueprints.Login.routes import login
    from CyberApp.blueprints.Core.routes import core
    from CyberApp.blueprints.Create_User.routes import signup
    from CyberApp.blueprints.Download_Info.routes import download_search
    from CyberApp.blueprints.User.routes import disp_user
    app.register_blueprint(login, url_prefix='/')
    app.register_blueprint(signup, url_prefix='/')
    app.register_blueprint(download_search, url_prefix='/')
    app.register_blueprint(disp_user, url_prefix='/login')
    app.register_blueprint(core)

    migrate = Migrate(app, db)

    return app
