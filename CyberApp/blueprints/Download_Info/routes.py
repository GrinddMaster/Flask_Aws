from flask import Blueprint, render_template, request, redirect, url_for
from CyberApp.blueprints.User.models import User

# TODO: When user searched should display Box with user email in the HTML
# TODO: When should display Box with user email in the HTML

download_search = Blueprint('download_search', __name__,
                            template_folder="templates")


@download_search.route('/search', methods=['GET', 'POST'])
def download():
    user_email = None
    if request.method == 'POST':
        username = request.form.get('search')
        user = User.query.filter_by(Name=username).first()
        if user:
            user_email = user.Email
    return render_template('downloadInfo.html', user_email=user_email)
