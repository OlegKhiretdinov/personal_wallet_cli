lint:
	poetry run flake8 personal_wallet

init_db:
	python3 db_init.py

install:
	poetry install

init: install init_db

wallet:
	poetry run python -m personal_wallet.scripts.wallet
