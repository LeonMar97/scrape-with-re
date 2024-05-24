install:poetry.lock pyproject.toml
	poetry install
run:
	poetry run python main.py
format:
	poetry run ruff format scrape_webz

lint:
	poetry run ruff check scrape_webz
lint-fix:
	poetry run ruff check --fix scrape_webz