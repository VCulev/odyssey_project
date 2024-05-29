from sanic import Sanic
from json import load
from app_config.routes import (get_all_movies, get_movies_by_year,
                               delete_movie, add_movies_by_year, update_movies_by_year)


def read_config() -> dict:
    with open("app_config/settings.json", "r") as file_handler:
        server_config = load(file_handler)
    return server_config


def get_app():
    sanic_app = Sanic("Movie_App")
    sanic_app.config.update(read_config())

    sanic_app.add_route(get_all_movies, "/movies", methods=["GET"])
    sanic_app.add_route(get_movies_by_year, "/movies/<year:int>", methods=["GET"])
    sanic_app.add_route(add_movies_by_year, "/movies/<year:int>", methods=["POST"])
    sanic_app.add_route(update_movies_by_year, "/movies/<year:int>", methods=["PUT"])
    sanic_app.add_route(delete_movie, "/movies/<year:int>/<name:str>", methods=["DELETE"])

    return sanic_app
