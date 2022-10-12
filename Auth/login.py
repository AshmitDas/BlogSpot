from flask import Blueprint, render_template, request, redirect, url_for, session
from Auth.check_user import Check_Credintials
from Auth.session import match_session_with_db, generate_sessionID, save_sessionID
from Auth.signup import sign_up


# login = Blueprint("login", __name__, static_folder="static", template_folder="templates")
login = Blueprint("login", __name__)


@login.route("/login",methods=["POST", "GET"])
def log_in():
    # session_obj = SessionID()

    if request.method == "POST":

        username = request.form["userName"]
        password = request.form["password"]

        creds = Check_Credintials(username, password)

        if creds.check_userid_exist():

            if creds.check_password():

                new_sessionID: str = generate_sessionID()
                save_sessionID(username, new_sessionID)
                session['sessionID'] = new_sessionID
                return redirect('/signup')

            else:
                return "Password".lower(), 401  # Unauthorized:  401

        else:
            return "UserID".lower(), 404  # Not found : 404

            

    if 'sessionID' in session:
        sessionID: str = session['sessionID']

        # if match_session_with_db(username, sessionID):
        #     # return redirect('/user/feed')
        #     return redirect('/')



    return render_template("Auth/login.html")