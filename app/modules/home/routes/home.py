
from flask import Blueprint
from app.modules.home.controllers.home import HomeController

home = Blueprint("home", __name__)


@home.route("/", methods=["GET", "POST"])
@home.route("/home", methods=["GET", "POST"])
def projects():
    return HomeController().projects()
