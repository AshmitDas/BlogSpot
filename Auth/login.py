from flask import Blueprint, render_template, request, redirect, url_for
from Auth.check_user import Check_Credintials
from Auth.signup import sign_up


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
                return redirect('/signup')
            else:
                return "Password".lower(), 401  # Unauthorized:  401

        else:
            return "UserID".lower(), 404  # Not found : 404


    return render_template("Auth/login.html")