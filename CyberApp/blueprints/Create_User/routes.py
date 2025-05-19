from flask import render_template, Blueprint, request, flash, redirect, url_for

signup = Blueprint('signup', __name__, template_folder='templates')
signup.secret_key = ' Hello World '


@signup.route('/Sign_up', methods=['GET', 'POST'])
def Sign_up():
    if request.method == 'POST':
        flash('Sign up Successful !')
        return redirect(url_for('login.login_page'))
    elif request.method == 'GET':
        return render_template('Sign_up.html')
