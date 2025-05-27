from flask import render_template, Blueprint, request, flash, redirect, url_for
from CyberApp.blueprints.User.models import User

login = Blueprint('login', __name__, template_folder='templates',
                  static_folder='static')


@login.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        check_user = User.query.filter_by(
            Name=username,
            Password=password).first()

        if check_user:
            return redirect(url_for('disp_user.display_info', name=username))
        else:
            flash("Doesn't exist")
            return redirect(url_for("login.login_page"))

    return render_template('Login.html')
