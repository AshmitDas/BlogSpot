from flask import Blueprint

settings = Blueprint("settings", __name__, static_folder="static", template_folder="templates")


def usr_settings():
    pass