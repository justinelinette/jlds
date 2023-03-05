from flask import render_template


class FilmScrobblerController():
    def page(self):
        return render_template("film_scrobbler.html", title="film scrobbler")
