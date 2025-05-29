from flask import render_template, Blueprint, request, flash, redirect, url_for, send_file, make_response
from CyberApp.blueprints.User.models import User, db
import os
import json

login = Blueprint('login', __name__, template_folder='templates', static_folder='static')

@login.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Vulnerable raw SQL query (SQLAlchemy 2.0+)
        query = f"SELECT * FROM Users WHERE Name = '{username}' AND Password = '{password}'"
        with db.engine.connect() as connection:
            check_user = connection.execute(db.text(query)).fetchone()

        if check_user:
            # Set cookie with username and loggedin=True
            response = make_response(redirect(url_for('disp_user.display_info', name=username)))
            response.set_cookie('auth', json.dumps({'username': username, 'loggedin': True}))
            return response
        else:
            # Set cookie with loggedin=False
            response = make_response(redirect(url_for('login.login_page')))
            response.set_cookie('auth', json.dumps({'username': '', 'loggedin': False}))
            flash("Doesn't exist")
            return response
    response = make_response(render_template('Login.html'))
    if 'auth' not in request.cookies:
        response.set_cookie('auth', json.dumps({'username': '', 'loggedin': False}))
    return response


@login.route('/download', methods=['GET'])
def download_file():
    filename = request.args.get('file')
    if not filename:
        return "Error: No file specified", 400

    # Vulnerable file traversal: path relative to CyberApp directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Points to CyberApp
    file_path = os.path.join(base_dir, 'Uploads', filename)

    print(f"Attempting to access file: {file_path}")  # Log for demo
    if os.path.exists(file_path):
        return send_file(file_path)
    else:
        return "File not found", 404
