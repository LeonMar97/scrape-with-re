# Scrape with re

This project is a web scraping tool that extracts data from two different forum platforms: phpBB and vBulletin. It utilizes Python's built-in `re` module for regular expression pattern matching to parse the HTML content of the forum pages.

## Prerequisites

- Python 3.x
- Poetry (Python dependency management tool)

## Project Structure
Project Structure
scrape-with-re/

├── scrape_webz/

    ├── data/
    ├── __init__.py
    └── post.py

    ├── scrapers/

    │   ├── __init__.py
    │   ├── phpbb_scraper.py
    │   ├── scraper_base.py
    │   └── vbulletin_scraper.py

    └── utils/
       ├── __init__.py
       ├── file_utils.py
       └── text_utils.py
 ── main.py
 ── README.md

- `data/`: Contains the `Post` class definition for representing forum posts.
- `scrape_webz/scrapers/`: Includes the base scraper class (`scraper_base.py`) and the specific scraper implementations for phpBB (`phpbb_scraper.py`) and vBulletin (`vbulletin_scraper.py`) forums.
- `scrape_webz/utils/`: Contains utility modules for file operations (`file_utils.py`) and text processing (`text_utils.py`) <b>also for date formating as requestd</b>.
- `main.py`: The main entry point of the application, where the scraping process is initiated.
- `Makefile`: Contains commands for running various tasks, such as installing dependencies, formatting, and linting.
- `pyproject.toml`: The Poetry configuration file for managing project dependencies.
- `poetry.lock`: The lockfile for reproducible dependency installations.
- `README.md`: This file, providing an overview of the project.

## Setup

1. Clone the repository or download the source code.
2. Install Poetry by following the instructions on the [Poetry documentation](https://python-poetry.org/docs/#installation).
3. Run the following command to install the project dependencies:



## Setup

1. Clone the repository or download the source code.
2. Install Poetry by following the instructions on the [Poetry documentation](https://python-poetry.org/docs/#installation).
3. Run the following command to install the project dependencies:
```bash
make install
```

## Usage
Run the following command to start the scraping process:
```bash
make run
```
    The scraped data will be saved as JSON files in the project directory, with filenames `phpbb_web.txt` and `vbulletin_web.txt`.

## Code Formatting and Linting

This project uses the `ruff` tool for code formatting and linting. You can use the following commands:

- Format the code:
```bash
make format
```
- lint the code:
```bash
make lint
```
- fix linting errors:
```bash
make lint-fix
```
# Notes
if it doesnt find scrapped data, it sets it as 'not found'.

# creator 
<b>Leon Markovich </b>