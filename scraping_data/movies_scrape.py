from bs4 import BeautifulSoup
import aiohttp


async def extract_movie_data_for_year(year: int) -> list:
    url = f'https://www.google.com/search?q=popular+movies+in+{year}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            html = await response.text()

    soup = BeautifulSoup(html, 'html.parser')

    movies = []

    movie_elements = soup.find_all('div', class_='UnFsfe cyKJce ZvGeOb')

    for element in movie_elements:
        name = element.text.strip()
        movies.append(name)

    return movies
