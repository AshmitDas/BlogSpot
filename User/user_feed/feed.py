from flask import Blueprint,redirect, render_template


feed = Blueprint("feed", __name__)


@feed.route("/feed")
def usr_feed():
    # TODO: Get username from Valid session
    # TODO: Get the latest posts.
    # TODO: Send the elements to template and render
    # TODO: Garmaramari kor
    return render_template("User/feed.html")