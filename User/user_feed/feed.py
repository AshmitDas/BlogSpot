from flask import Blueprint,redirect, render_template, session
from sqlalchemy import select, update, func
from sqlalchemy.orm import Session, Query
from database.db import User, Blog, engine
from Auth.login import SESSION_ID
import os


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



    # users_sessionID = mysession['sessionID']
    
    # query_stmt = select(User.session_id).where(User.session_id == users_sessionID)

    # with Session(engine) as session:
    #     try:
    #         result = session.execute(query_stmt).fetchone()[0]

    #         if result == users_sessionID:
    #             return "OK", 202

    #     except TypeError:
    #         return "ERROR", 401

    Posts = {}

    latest_post_id = Session(engine).execute(func.max(Blog.fetch_id)).fetchone()[0]

    counter = 1

    while True: 
        if counter > 5:
            break

        else:
            query_stmt = select(Blog).where(Blog.fetch_id == latest_post_id)

            try:
                for row in Session(engine).execute(query_stmt):
                    post_details = [row[0].user_id, row[0].fetch_id, row[0].title, row[0].description, row[0].time_created]
                    Posts[f"User {counter}"] = makeDictionary(post_details, row[0].filename, row[0].filetype)
                    counter += 1
                    latest_post_id -= 1

            except TypeError:
                break

        
    print(Posts)

    return render_template("User/feed.html")




def makeDictionary(post_details, filename, filetype):
    keys = ["userID", "fetchID", "title", "body", "timestamp"]

    post_dict = { k:v for (k,v) in zip(keys, post_details)}

    if filename == "":
        post_dict["media_src"] = None
        return post_dict

    else:
        if filetype in ["jpeg", "jpg"]:
            post_dict["media_src"] = os.getcwd() + "media_files/Image/" + filename + "." + filetype
            post_dict["media_type"] = "Image"
            return post_dict

        else:
            post_dict["media_src"] = os.getcwd() + "media_files/Video/" + filename + "." + filetype
            post_dict["media_type"] = "Video"
            return post_dict
