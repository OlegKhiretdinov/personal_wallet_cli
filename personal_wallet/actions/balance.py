import json

from personal_wallet.localization import BALANCE
from personal_wallet.settings import WALLET_OPERATION_LOG_PATH


def get_balance():
    with open(WALLET_OPERATION_LOG_PATH, 'r') as f:
        balance = json.loads(f.read())['total']

    print(f'{BALANCE}: {balance}')
