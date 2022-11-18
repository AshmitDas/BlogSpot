from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import insert
from database.db import User, engine
from Auth.check_user import Check


signup = Blueprint("signup", __name__)


@signup.route("/signup", methods=["POST", "GET"])
def sign_up():
    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        firstname = request.form["firstname"].capitalize()
        lastname = request.form["lastname"].capitalize()


        if not Check.userid_exist(username):

            query_stmt = insert(User).values(user_id = username, password = password, firstname = firstname, lastname=lastname)

            with engine.connect() as conn:
                conn.execute(query_stmt)
                conn.commit()
            
            return redirect("/login")

        else:
             return "UserID already exists!", 409  # conflict: 409


    return render_template("Auth/signup.html")