populate:
	poetry run python src/stock_data_project/pipelines/jobs/populate_database.py

test_units:
	poetry run pytest tests/units/*

test_integrations:
	poetry run pytest tests/integrations/

update_db_schema:
	poetry run python scripts/create_database.py
	sqlite3 app.db ".schema" > devops/db/current_schema/schema.sql

format_all: 
	poetry run black src/*
	poetry run black tests/*
	poetry run isort --filter-files tests/*
	poetry run isort --filter-files src/*

lint: 
	poetry run flake8 src tests

all: test_units format_all lint
