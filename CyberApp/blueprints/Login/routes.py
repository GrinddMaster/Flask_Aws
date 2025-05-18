from flask import render_template, Blueprint

login = Blueprint('login', __name__, template_folder='templates',
                  static_folder='static')


@login.route('/login')
def login_page():
    return render_template('Login.html')
