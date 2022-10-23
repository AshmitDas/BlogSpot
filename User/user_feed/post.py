from flask import Blueprint, redirect, request, url_for, session
from werkzeug.utils import secure_filename
from User.user_feed.generate_filename import filename
from Auth.login import SESSION_ID
from User.user_feed.save_to_db import *
import shutil


post = Blueprint("post", __name__)


@post.route("/post", methods=['GET', 'POST'])
def post_blog():
    if request.method == 'POST':
        title = request.form['Title']
        description = request.form['Description']
        media = request.files['media']

        media_info = media.filename.split(".")

        media_info[0] = filename()    # FIXME: ...asa.sd.fas.df.as.dfa.sdf.asd...jpg

        media.filename = ".".join[media_info]

        media.save(media.filename)

        save_to_media_db(media_info[0], media_info[1], SESSION_ID)
        # save_to_blog_db(title, description, SESSION_ID)




    return redirect(url_for('feed.usr_feed'))