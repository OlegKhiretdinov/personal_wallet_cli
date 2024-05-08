from enum import Enum

WALLET_OPERATION_LOG_PATH = 'personal_wallet/db/operations.json'

DATE_FORMAT = '%Y-%m-%d'

QUIT_COMMAND = 'q'


class OperationType(Enum):
    INCOME = '1'
    EXPENDITURE = '2'


class ActionType(Enum):
    ADD = '1'
    EDIT = '2'
    TOTAL = '3'
    SEARCH = '4'
