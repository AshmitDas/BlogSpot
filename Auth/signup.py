from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import insert
from database.db import User, engine
from Auth.check_user import Check


signup = Blueprint("signup", __name__)


@signup.route("/signup", methods=["POST", "GET"])
def sign_up():
    if request.method == "POST":

        username = request.form["userName"]
        password = request.form["password"]

        firstName = request.form["firstName"].capitalize()
        lastName = request.form["lastName"].capitalize()


        if not Check.userid_exist(username):

            query_stmt = insert(User).values(user_id = username, password = password, firstname = firstName, lastname=lastName)

            with engine.connect() as conn:
                conn.execute(query_stmt)
                conn.commit()
            
            return redirect("/login")

        else:
             return "UserID already exists!", 409  # conflict: 409


    return render_template("Auth/signup.html")