import httpx
import pytest

BASE_URL = "http://localhost:8000"


@pytest.mark.asyncio
async def test_post_movies():
    async with httpx.AsyncClient() as client:
        year = 2021
        response = await client.post(f"{BASE_URL}/movies/{year}")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0


@pytest.mark.asyncio
async def test_get_movies_by_year():
    async with httpx.AsyncClient() as client:
        year = 2021
        response = await client.get(f"{BASE_URL}/movies/{year}")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)


@pytest.mark.asyncio
async def test_get_all_movies():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/movies")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_put_movies():
    async with httpx.AsyncClient() as client:
        year = 2021
        response = await client.put(f"{BASE_URL}/movies/{year}")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0


@pytest.mark.asyncio
async def test_delete_movie():
    async with httpx.AsyncClient() as client:
        year = 2021
        name = "Poveste din cartierul de vest"
        response = await client.delete(f"{BASE_URL}/movies/{year}/{name}")
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == name

        response = await client.delete(f"{BASE_URL}/movies/{year}/NonExistentMovie")
        assert response.status_code == 404
        data = response.json()
        assert data["message"] == f"Movie 'NonExistentMovie' not found for year {year}"
