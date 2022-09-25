from flask import Blueprint, render_template, request, redirect, url_for
from Auth.check_user import Check_Credintials


# login = Blueprint("login", __name__, static_folder="static", template_folder="templates")
login = Blueprint("login", __name__)


@login.route("/login",methods=["POST", "GET"])
def log_in():
    if request.method == "POST":

        username = request.form["userName"]
        password = request.form["password"]

        creds = Check_Credintials(username, password)

        if creds.check_userid_exist():

            if creds.check_password(): 
                return redirect()
            else:
                return "<h2>Wrong password</h2>"

        else:
            return "<h2>User does not exist</h2>"


    return render_template("Auth/login.html")