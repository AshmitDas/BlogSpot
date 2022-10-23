from flask import Blueprint, render_template, request, redirect, url_for, session
from Auth.check_user import Check
from Auth.session import SessionID
from Auth.signup import sign_up

SESSION_ID = 'sessionID'

login = Blueprint("login", __name__)


@login.route("/login", methods=["POST", "GET"])
def log_in():

    if request.method == "POST":

        username = request.form["userName"]
        password = request.form["password"]

        if Check.userid_exist(username):

            if Check.password_matches(username, password):

                if SESSION_ID in session:
                    users_sessionID: str = session[SESSION_ID]

                    if SessionID.match_with_db(username, users_sessionID):
                        return redirect("/feed")

                new_sessionID: str = SessionID.generate()
                SessionID.save(username, new_sessionID)
                session[SESSION_ID] = new_sessionID
                return redirect("/feed")

            else:
                return "Password".lower(), 401  # Unauthorized:  401

        else:
            return "UserID".lower(), 404  # Not found : 404


    return render_template("Auth/login.html")