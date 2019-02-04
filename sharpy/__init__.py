import vk
from flask import Flask

from sharpy import database
from .responses import responses_collection

session = vk.Session()
api = vk.API(session, v='5.92')

database.init()

responses_collection.init()


def create_app():
    app = Flask(__name__)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
