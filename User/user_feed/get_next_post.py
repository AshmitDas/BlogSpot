from flask import Blueprint,redirect, render_template, session, jsonify, request
from sqlalchemy import select, update, func
from sqlalchemy.orm import Session, Query
from database.db import User, Blog, engine


get_next_post = Blueprint("get_next_post", __name__)


@get_next_post.route("/feed/get_next_post")
def getnextpost():

    usr_post = {}

    blogID = request.args.get('ID')
    

    query_stmt = select(Blog).where(Blog.fetch_id < blogID).order_by(Blog.fetch_id.desc()).limit(1)

    for row in Session(engine).execute(query_stmt):
        if row is not None:
            post_details = [row[0].user_id, row[0].fetch_id, row[0].title, row[0].description, row[0].time_created.strftime("%m-%d-%Y %H:%M:%S")]
            usr_post = makeDictionary(post_details, row[0].filename, row[0].filetype)

            return jsonify(usr_post)

        
    return jsonify({}), 404



def makeDictionary(post_details, filename, filetype):
    keys = ["userID", "fetchID", "title", "body", "timestamp"]

    # print(post_details[-1])

    post_dict = { k:v for (k,v) in zip(keys, post_details)}

    if filename == "":
        post_dict["media_src"] = None
        post_dict["media_type"] = None
        return post_dict

    else:
        if filetype in ["jpeg", "jpg"]:
            post_dict["media_src"] = "static/media_files/Image/" + filename + "." + filetype
            post_dict["media_type"] = "Image"
            return post_dict

        else:
            post_dict["media_src"] = "static/media_files/Video/" + filename + "." + filetype
            post_dict["media_type"] = "Video"
            return post_dict