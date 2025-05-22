from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import migrate
import urllib.parse

db = SQLAlchemy()
username = ''
password = ''
host = 'localhost'
port = '3306'
database_name = ''

encoded_password = urllib.parse.quote_plus(password)

def Create_app():
    app = Flask(__name__)
    app.secret_key = " Test key"
    app.config['SQLAlchemy_DATABASE_URI'] = 'MySql://'
    from CyberApp.blueprints.Login.routes import login
    db.init_app(app)

    from CyberApp.blueprints.Core.routes import core
    from CyberApp.blueprints.Create_User.routes import signup
    from CyberApp.blueprints.Download_Info.routes import download_search
    app.register_blueprint(login, url_prefix='/')
    app.register_blueprint(signup, url_prefix='/')
    app.register_blueprint(download_search, url_prefix='/')
    app.register_blueprint(core)

    Migrate = migrate(app, db)

    return app
