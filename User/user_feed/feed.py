from flask import Blueprint,redirect


feed = Blueprint("feed", __name__, static_folder="static", template_folder="templates")


@feed.route("/feed", methods=["POST", "GET"])
@feed.route("/feed/<usrnm>", methods=["POST", "GET"])
def usr_feed(usrnm):
    return redirect("")