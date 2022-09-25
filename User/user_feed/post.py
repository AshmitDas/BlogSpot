from flask import Blueprint, redirect, render_template

post = Blueprint("post", __name__, static_folder="static", template_folder="templates")


@post.route("/feed/post")
def post_blog():
    return render_template("post_blog.html")