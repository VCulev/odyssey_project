from typing import List, Dict
from sanic import Sanic, response
from json import dump, load
from urllib.parse import unquote
from scraping_data.movies_scrape import extract_movie_data_for_year
from process_data.data_process import (extract_name, extract_genre,
                                       extract_movie_type, extract_duration_period)

app = Sanic("movie-app")


def load_movies() -> Dict[str, List[Dict]]:
    try:
        with open('movies.json', 'r') as file:
            return load(file)
    except FileNotFoundError:
        return {}


def save_movies(movies: Dict[str, List[Dict]]):
    with open('movies.json', 'w') as file:
        dump(movies, file, indent=4)


async def fetch_movie_data_for_year(year: int) -> List[Dict]:
    response_movies = await extract_movie_data_for_year(year)
    movies = []
    for movie in response_movies:
        movie_type = extract_movie_type(movie)
        duration_period = extract_duration_period(movie)
        name = extract_name(movie, movie_type)
        genre = extract_genre(movie)
        movies.append(
            {
                'name': name,
                'type': movie_type,
                'duration': duration_period,
                'genre': genre
            }
        )
    return movies


@app.post("/movies/<year:int>")
async def add_movies_by_year(request, year: int) -> response.HTTPResponse:
    try:
        new_movies = await fetch_movie_data_for_year(year)

        save_movies({str(year): new_movies})

        return response.json(new_movies, status=200)

    except Exception as e:
        return response.json({"error": str(e)}, status=500)


@app.get("/movies/<year:int>")
async def get_movies_by_year(request, year: int) -> response.HTTPResponse:
    try:
        movies = load_movies()
        if str(year) in movies:
            return response.json(movies[str(year)], status=200)

        return response.json({"message": f"Movies not found for year {year}"}, status=404)

    except Exception as e:
        return response.json({"error": str(e)}, status=500)


@app.get("/movies")
async def get_all_movies(request) -> response.HTTPResponse:
    try:
        movies = load_movies()
        return response.json(movies, status=200)

    except Exception as e:
        return response.json({"error": str(e)}, status=500)


async def update_movies_by_year(request, year: int) -> response.HTTPResponse:
    try:
        new_movies = await fetch_movie_data_for_year(year)

        movies = load_movies()

        movies[str(year)] = new_movies

        save_movies(movies)

        return response.json(new_movies, status=200)

    except Exception as e:
        return response.json({"error": str(e)}, status=500)


@app.delete("/movies/<year:int>/<name:str>")
async def delete_movie(request, year: int, name: str) -> response.HTTPResponse:
    try:
        movies = load_movies()
        if str(year) in movies:
            decoded_name = unquote(name)
            for i, movie in enumerate(movies[str(year)]):
                if movie['name'].lower() == decoded_name.lower():
                    deleted_movie = movies[str(year)].pop(i)
                    save_movies(movies)
                    return response.json(deleted_movie, status=200)

            return response.json({"message": f"Movie '{decoded_name}' not found for year {year}"}, status=404)

        return response.json({"message": f"Movies not found for year {year}"}, status=404)

    except Exception as e:
        return response.json({"error": str(e)}, status=500)