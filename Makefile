install:poetry.lock pyproject.toml
	poetry install
run:
	poetry run python scrape_webz\scrapers\scrape.py