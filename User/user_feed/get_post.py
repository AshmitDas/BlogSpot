from flask import Blueprint,redirect, render_template, session, jsonify
from sqlalchemy import select, update, func
from sqlalchemy.orm import Session, Query
from database.db import User, Blog, engine
import os, datetime


getpost = Blueprint("getpost", __name__)


@getpost.route("/feed/getpost")
def get_post():

    # posts = {}

    # last_post_id = Session(engine).execute(func.max(Blog.fetch_id)).fetchone()[0]

    # # no posts present
    # if last_post_id ==  None:
    #     print("No posts.")
    #     return jsonify({}), 404

    # # when posts are present.
    # else:

    #     counter = 1
    #     last_post_id += 1

    #     while counter <= 5: 

    #         query_stmt = select(Blog).where(Blog.fetch_id < last_post_id).order_by(Blog.fetch_id.desc()).limit(1)

    #         try:
    #             for row in Session(engine).execute(query_stmt):
    #                 post_details = [
    #                                     row[0].user_id, 
    #                                     row[0].fetch_id, 
    #                                     row[0].title, 
    #                                     row[0].description, 
    #                                     row[0].time_created.strftime("%m-%d-%Y %H:%M:%S")
    #                                 ]
    #                 """
    #                     {
    #                         'blog 1': {'title': 'asldkfjalskdjf', ...},
    #                         'blog 2': {'title': 'asldkfjalskdjf', ...},
    #                         'blog 3': {'title': 'asldkfjalskdjf', ...},
    #                     }
    #                 """
    #                 posts[f"blog {counter}"] = makeDictionary(post_details, row[0].filename, row[0].filetype)
    #                 counter += 1
    #                 last_post_id = row[0].fetch_id
    #                 # print("inside: ", posts)

    #         except TypeError:
    #             break

    #     # posts = jsonify(posts)
    #     print(posts)
    #     return jsonify(posts)
    return jsonify({"name": "rintu"})



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