import os
from dotenv import load_dotenv, find_dotenv


class Config():
    APP_NAME = "justinelinette"
    SECRET_KEY = os.environ.get("SECRET_KEY")

    def __init__(self):
        load_dotenv(find_dotenv())
