lint:
	poetry run flake8 personal_wallet

wallet:
	poetry run python -m personal_wallet.scripts.wallet
