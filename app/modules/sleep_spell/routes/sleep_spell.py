
from flask import Blueprint
from app.modules.sleep_spell.controllers.sleep_spell import SleepSpellController


sleep_spell = Blueprint("sleep_spell", __name__)


@sleep_spell.route("/sleep_spell", methods=["GET", "POST"])
def form():
    return SleepSpellController().form()


@sleep_spell.route("/result", methods=["POST"])
def result():
    return SleepSpellController().result()
