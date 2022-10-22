from flask import Blueprint, redirect, request, url_for, session
from werkzeug.utils import secure_filename
from User.user_feed.generate_filename import filename
from Auth.login import sessionID
from User.user_feed.save_to_db import Save

post = Blueprint("post", __name__)




@post.route("/post", methods=['GET', 'POST'])
def post_blog():
    if request.method == 'POST':
        title = request.form['Title']
        description = request.form['Description']
        media = request.files['media']

        media_info = media.filename.split(".")

        media_info[0] = filename()

        Save.to_media_db(media_info[0], media_info[1], sessionID)
        Save.to_blog_db(title, description, sessionID)





    return redirect(url_for('feed.usr_feed'))