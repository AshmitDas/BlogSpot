from flask import Blueprint, render_template, request, redirect, url_for, session
from Auth.check_user import Check
from Auth.session import SessionID
from Auth.signup import sign_up

sessionID = 'sessionID'

# login = Blueprint("login", __name__, static_folder="static", template_folder="templates")
login = Blueprint("login", __name__)


@login.route("/login",methods=["POST", "GET"])
def log_in():

    if request.method == "POST":

        username = request.form["userName"]
        password = request.form["password"]

        if Check.userid_exist(username):

            if Check.password_matches(username, password):

                if sessionID in session:
                    sessionID: str = session[sessionID]

                    if SessionID.match_session_with_db(username, sessionID):
                        return redirect("/users/feed")
                    else:
                        new_sessionID: str = SessionID.generate_sessionID()
                        SessionID.save_sessionID(username, new_sessionID)
                        session[sessionID] = new_sessionID
                        return("/users/feed")

                else:
                    new_sessionID: str = SessionID.generate_sessionID()
                    SessionID.save_sessionID(username, new_sessionID)
                    session[sessionID] = new_sessionID
                    return redirect('/users/feed')

            else:
                return "Password".lower(), 401  # Unauthorized:  401

        else:
            return "UserID".lower(), 404  # Not found : 404


    return render_template("Auth/login.html")