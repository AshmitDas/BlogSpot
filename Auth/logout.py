from flask import Blueprint, session, redirect

logout = Blueprint("logout", __name__)

@logout.route("/logout")
def log_out():
    if 'sessionID' in session:
        session.pop('sessionID')

    return redirect("/login")
