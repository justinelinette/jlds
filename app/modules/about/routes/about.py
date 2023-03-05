from flask import Blueprint
from app.modules.about.controllers.about import AboutController


about = Blueprint("about", __name__)


@about.route("/about", methods=["GET", "POST"])
def page():
    return AboutController().page()
