# Odyssey Project

> ⚠️ This repository is strictly for demonstration purposes and is not meant for you (as a bootcamp participant) to copy from. Use it wisely and get some inspiration, but do not copy-paste. The current state can be improved and there are a lot of ways to do so.
Don't be limited by this codebase, be creative and make it your own.

The Odyssey Project is a comprehensive movie recommendation system built with Python. It involves web scraping, data processing, data storage, API creation, and testing, all following clean code principles.

## Project Description

The Odyssey Project is designed to provide movie recommendations by scraping popular movie data from Google Search, processing this data for consistency, and storing it in a JSON file. An API is created to interact with this data, allowing users to retrieve, add, update, and delete movie records. The project includes comprehensive testing to ensure data integrity and code quality. All dependencies are managed in a virtual environment, and the project emphasizes clean code principles. Additionally, the scraping process is optimized with parallelization for efficiency.

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/eduard-balamatiuc/odyssey_project.git
    cd odyssey_project
    ```

2. **Create a Virtual Environment**
    ```bash
    python3.12 -m venv venv
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

## File Structure

```
odyssey_project/
├── README.md
├── requirements.txt
├── scraper.py
├── data_processing.py
├── api.py
├── test_data_processing.py
└──data_storage/
    └── movies.json
```
