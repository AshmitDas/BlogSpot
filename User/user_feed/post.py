from flask import Blueprint, redirect, request, url_for
from werkzeug.utils import secure_filename
from User.user_feed.generate_filename import filename


post = Blueprint("post", __name__)




@post.route("/post", methods=['GET', 'POST'])
def post_blog():
    if request.method == 'POST':
        title = request.form['Title']
        description = request.form['Description']
        media = request.files['media']

        media_info = media.filename.split(".")

        media_info[0] = filename()

        print(media_info)





    return redirect(url_for('feed.usr_feed'))