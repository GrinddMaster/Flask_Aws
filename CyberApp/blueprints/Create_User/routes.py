from flask import render_template, Blueprint, request, flash, redirect, url_for
from CyberApp.blueprints.User.models import User
from werkzeug.security import generate_password_hash
from CyberApp.app import db

signup = Blueprint('signup', __name__, template_folder='templates')
signup.secret_key = ' Hello World '


@signup.route('/Sign_up', methods=['GET', 'POST'])
def Sign_up():
    if request.method == 'POST':
        flash('Sign up Successful !')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        regist_user = User.query.filter_by(Name=username).first()

        if regist_user:
            flash("User already exists ! ")
            return redirect(url_for(signup.Sign_up))
        hashed_pass = generate_password_hash(
            password, method="pbkdf2:sha256", salt_length=8)
        new_user = User(Name=username,
                        Password=hashed_pass,
                        Email=email)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login.login_page'))
    elif request.method == 'GET':
        return render_template('Sign_up.html')
