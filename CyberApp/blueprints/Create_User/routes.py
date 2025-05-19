from flask import Blueprint, render_template


signup = Blueprint('signup', __name__, template_folder='templates')


@signup.route('/Sign_up', methods=['GET'])
def Sign_up():
    return render_template('Sign_up.html')
