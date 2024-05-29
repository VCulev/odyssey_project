import re


def extract_movie_type(entry: str) -> str:
    movie_types = ['PG-13', 'Not Rated (USA)', 'NR', 'R', 'G']
    movie_type = "Unknown"

    for mt in movie_types:
        if mt in entry:
            movie_type = mt
            break

    return movie_type


def extract_duration_period(entry: str) -> tuple:
    duration_period = None
    duration_period_match = re.search(r"(\d{1})\xa0h (\d{1,2})\xa0min", entry)
    if duration_period_match:
        duration_period = (duration_period_match.group(1).strip() + "h", duration_period_match.group(2).strip() + "min")
    else:
        duration_period_match = re.search(r"(\d{1})\xa0ore", entry)
        if duration_period_match:
            duration_period = (duration_period_match.group(1).strip() + "h", "0min")
    return duration_period


def extract_name(entry: str, movie_type="Unknown") -> str:
    if movie_type != "Unknown":
        name = entry.split(movie_type)[0].strip()
    else:
        name = re.search(r"^(.*?)(?=\d)", entry)
        if name:
            return name.group(0).strip()
    return name


def extract_genre(entry: str) -> str:
    genre = entry.split('.')[-1].strip()
    return genre