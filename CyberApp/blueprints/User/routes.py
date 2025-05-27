from flask import render_template, Blueprint

disp_user = Blueprint("disp_user", __name__, template_folder="templates")


@disp_user.route("/<name>")
def display_info(name):
    return render_template("user_template.html", person={name})
