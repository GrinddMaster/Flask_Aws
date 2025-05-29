from flask import Flask
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import urllib.parse

load_dotenv()
# avoid hard coding credentials create a .env file and put them there.
# Make sure they're ignored by git
required_vars = ["DB_USERNAME", "DB_PASSWORD", "DB_HOST", "DB_PORT", "DB_NAME", "SECRET_KEY"]
for var in required_vars:
    if not os.getenv(var):
        raise EnvironmentError(f"Missing required environment variable: {var}")

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database_name = os.getenv("DB_NAME")
db = SQLAlchemy()

encoded_password = urllib.parse.quote_plus(str(password))


def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")
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
