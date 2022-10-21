from flask import Blueprint, redirect, request, url_for


post = Blueprint("post", __name__, static_folder="static", template_folder="templates")



@post.route("/post", methods=['GET', 'POST'])
def post_blog():
    if request.method == 'POST':
        title = request.form['Title']
        description = request.form['Description']
        media = request.files['media']

        media.save(media.filename)

        print("received")




    return redirect(url_for('feed.usr_feed'))