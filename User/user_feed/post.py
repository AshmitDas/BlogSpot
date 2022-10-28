from flask import Blueprint, redirect, request, url_for, session
from werkzeug.utils import secure_filename
from User.user_feed.generate_filename import generate_filename
from Auth.login import SESSION_ID
from User.user_feed.save_to_db import *
import shutil


post = Blueprint("post", __name__)

img = ['jpg', 'jpeg']


@post.route("/post", methods=['GET', 'POST'])
def post_blog():
    if request.method == 'POST':
        title = request.form['Title']
        description = request.form['Description']
        media = request.files['media']

        if media.filename == "":

            save_to_media_db(SESSION_ID)
            save_to_blog_db(title, description, SESSION_ID)

        else:
            media_info = media.filename.split(".")

            if media.filename.count(".") != 1 or media_info[0] == "":
                return "Invalid Filename", 400

            media_info[0] = generate_filename()    # FIXME: ...asa.sd.fas.df.as.dfa.sdf.asd...jpg
            media.filename = ".".join(media_info)
            media.save(media.filename)

            save_to_media_db(SESSION_ID, media_info[0], media_info[1])
            save_to_blog_db(title, description, SESSION_ID, media_info[0], media_info[1])

            current_location = media.filename
            destination_location = "~/Projects/BlogSpot/media_files/"

            if media_info[1] in img:
                shutil.move(current_location, destination_location + "Image/" + media.filename)
            else:
                shutil.move(current_location, destination_location + "Video/" + media.filename)



    return redirect(url_for('feed.usr_feed'))