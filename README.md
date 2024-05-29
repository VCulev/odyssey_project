# Odyssey Project


The Odyssey Project is a comprehensive movie recommendation system built with Python. It involves web scraping, data processing, data storage, API creation, and testing, all following clean code principles.

## Project Description

The Odyssey Project is designed to provide movie recommendations by scraping popular movie data from Google Search, processing this data for consistency, and storing it in a JSON file. An API is created to interact with this data, allowing users to retrieve, add, update, and delete movie records. The project includes comprehensive testing to ensure data integrity and code quality. All dependencies are managed in a virtual environment, and the project emphasizes clean code principles. Additionally, the scraping process is optimized with parallelization for efficiency.

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/VCulev/odyssey_project.git
    cd odyssey_project
    ```

2. **Create a Virtual Environment**
    ```bash
    python3.11 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Project
```bash
python main.py
```

## Runing Tests

```bash
cd tests
pytest test_api_routes.py
```
Make sure the server is running
## File Structure

```
odyssey_project/
│
├── app_config/
│   ├── __init__.py
│   ├── configure.py
│   ├── routes.py
│   └── settings.json
│
├── process_data/
│   ├── __init__.py
│   └── data_process.py
│
├── scraping_data/
│   ├── __init__.py
│   └── movies_scrape.py
│
├── tests/
│   ├── __init__.py
│   └── test_api_routes.py
│
├── .gitignore
├── main.py
├── movies.json
└── README.md
```
