from flask import Blueprint, render_template

download_search = Blueprint('download_search', __name__,
                            template_folder="templates")


@download_search.route('/search')
def download(uid):
    return render_template('downloadInfo.html')
