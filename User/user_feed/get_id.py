from flask import Blueprint,redirect, render_template, session, jsonify
from sqlalchemy import select, update, func
from sqlalchemy.orm import Session, Query
from database.db import User, Blog, engine
import os, datetime


getID = Blueprint("getID", __name__)


@getID.route("/feed/getID")
def get_id():

    id = Session(engine).execute(func.max(Blog.fetch_id)).fetchone()[0]

    if id == None:
        return jsonify({}), 400
    else:
        return jsonify({"id" : id}), 200
