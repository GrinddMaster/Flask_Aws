from flask import Blueprint, redirect, url_for

core = Blueprint('core', __name__)


@core.route('/')
def core_route():

    return redirect(url_for('login.login_page'))
