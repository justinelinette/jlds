from flask import render_template


class AboutController():
    def page(self):
        return render_template("about.html", title="about")
