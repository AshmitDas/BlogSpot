from flask import Blueprint,redirect, render_template, session, jsonify
from sqlalchemy import select, update, func
from sqlalchemy.orm import Session, Query
from database.db import User, Blog, engine
from Auth.login import SESSION_ID
import os, datetime


mysession = session

feed = Blueprint("feed", __name__)


@feed.route("/feed", methods = ["GET"])
def usr_feed():

    # print(mysession['sessionID'])

    # TODO: Get username from Valid session
    # TODO: Get the latest posts.
    # TODO: Send the elements to template and render
    # TODO: Garmaramari kor

    # query_stmt = select(Blog.fetch_id).order_by(Blog.fetch_id.desc())

    # with Session(engine) as session:
    #     result = session.execute(query_stmt).fetchall()[0][1]
    #     print(result)

    users_sessionID = mysession['sessionID']
    
    query_stmt = select(User.session_id).where(User.session_id == users_sessionID)

    with Session(engine) as session:
        try:
            result = session.execute(query_stmt).fetchone()[0]

            if result == users_sessionID:
                return render_template("User/feed.html")

        except TypeError:
            return redirect("/login")
