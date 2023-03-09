from flask import render_template


class SleepBotController():
    def page(self):
        return render_template("sleep_bot.html", title="sleepbot")
