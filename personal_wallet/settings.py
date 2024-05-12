from enum import Enum

WALLET_OPERATION_LOG_PATH = 'personal_wallet/db/operations.json'

DATE_FORMAT = '%Y-%m-%d'

QUIT_COMMAND = 'q'
SEARCH_COMMAND = 's'
SEARCH_BALANCE_COMMAND = 'sb'
CANCEL_COMMAND = 'c'


class OperationType(Enum):
    INCOME = '1'
    EXPENDITURE = '2'


class ActionType(Enum):
    ADD = '1'
    EDIT = '2'
    TOTAL = '3'
    SEARCH = '4'


# Поля записей в БД
class DBOperationsFields(Enum):
    DATE = 'date'
    AMOUNT = 'amount'
    OPERATION = 'operation'
    DESCRIPTION = 'description'


# Поля по которым можно вести поиск
class SearchFields(Enum):
    DATE = '1'
    AMOUNT = '2'
    OPERATION = '3'


# Соответствие полей БД и полей поиска
SearchDbFieldsMap = {
    SearchFields.DATE.value: DBOperationsFields.DATE.value,
    SearchFields.AMOUNT.value: DBOperationsFields.AMOUNT.value,
    SearchFields.OPERATION.value: DBOperationsFields.OPERATION.value
}


class FilterItemFields(Enum):
    FIELD = 'field'
    OPERATOR = 'operator'
    CONDITION = 'condition'
