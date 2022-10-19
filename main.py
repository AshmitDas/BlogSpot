from flask import Flask, redirect, render_template, url_for
from Auth.login import login
from Auth.signup import signup
from Auth.logout import logout
from User.user_feed.feed import feed
from User.user_feed.post import post

app = Flask(__name__)

app.config["SECRET_KEY"] = "hello"

app.register_blueprint(login, url_prefix="/")
app.register_blueprint(logout, url_prefix="/")
app.register_blueprint(signup, url_prefix="/")
app.register_blueprint(feed, url_prefix="/")
app.register_blueprint(post, url_prefix="/")

@app.route("/")
def home():
    # return redirect(url_for("login.log_in"))
    return render_template("Home/home.html")


if __name__ == "__main__":
    app.run(debug=True)