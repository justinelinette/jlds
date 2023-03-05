from flask import Blueprint
from app.modules.film_scrobbler.controllers.film_scrobbler import FilmScrobblerController


film_scrobbler = Blueprint("film_scrobbler", __name__)


@film_scrobbler.route("/film_scrobbler", methods=["GET", "POST"])
def page():
    return FilmScrobblerController().page()
