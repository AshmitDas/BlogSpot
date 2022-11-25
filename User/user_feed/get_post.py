from flask import Blueprint,redirect, render_template, session, jsonify
from sqlalchemy import select, update, func
from sqlalchemy.orm import Session, Query
from database.db import User, Blog, engine
import os, datetime


getpost = Blueprint("getpost", __name__)


@getpost.route("/feed/getpost")
def get_post():

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
                    post_details = [row[0].user_id, row[0].fetch_id, row[0].title, row[0].description, row[0].time_created.strftime("%m-%d-%Y %H:%M:%S")]
                    Posts[f"blog {counter}"] = makeDictionary(post_details, row[0].filename, row[0].filetype)
                    counter += 1
                    latest_post_id -= 1

            except TypeError:
                break
    
    return jsonify(Posts)





def makeDictionary(post_details, filename, filetype):
    keys = ["userID", "fetchID", "title", "body", "timestamp"]

    # print(post_details[-1])

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