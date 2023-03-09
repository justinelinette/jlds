from flask import Blueprint
from app.modules.sleep_bot.controllers.sleep_bot import SleepBotController


sleep_bot = Blueprint("sleep_bot", __name__)


@sleep_bot.route("/spell_bot", methods=["GET", "POST"])
def page():
    return SleepBotController().page()
