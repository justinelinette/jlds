import os
from dotenv import load_dotenv, find_dotenv


class Config():
    APP_NAME = "justinelinette"
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

    def __init__(self):
        load_dotenv(find_dotenv())
