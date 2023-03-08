from flask import Flask
from app.modules.sleep_spell.models.bot import Bot
import subprocess


def create_app():
    # subprocess.run(["pip", "install", "--upgrade", "pip"], capture_output=True)
    app = Flask(__name__)
    with app.app_context():
        from app.config.config import Config
        app.config.from_object(Config)
        from app.modules.home.routes.home import home
        from app.modules.about.routes.about import about
        from app.modules.sleep_spell.routes.sleep_spell import sleep_spell
        from app.modules.film_scrobbler.routes.film_scrobbler import film_scrobbler
        app.register_blueprint(home)
        app.register_blueprint(about)
        app.register_blueprint(sleep_spell)
        app.register_blueprint(film_scrobbler)
        return app


Bot.start_threading()
