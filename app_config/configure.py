from sanic import Sanic
from json import load
from routes import add_movie


def read_config() -> dict:
    file_handler = open("settings.json", "r")
    server_config = load(file_handler)
    file_handler.close()
    return server_config


def get_app():
    sanic_app = Sanic("Movie_App")
    sanic_app.config.update(read_config())

    sanic_app.add_route(add_movie, "/api/movie", methods=["POST"], ctx_refsanic=sanic_app)

    return sanic_app
