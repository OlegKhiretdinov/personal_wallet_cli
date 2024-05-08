from personal_wallet.settings import ActionType, OperationType

WELCOME_TEXT = 'Personal Wallet v 0.1.0'
SELECT_ACTON = 'ВЫБЕРИТЕ ДЕЙСТВИЕ \n'
USER_DATE = 'Введите дату в формате YYYY-MM-DD'
INSERT_DATA_DEFAULT = 'Если оставить пустым подставится текущая дата: '
SELECT_CATEGORY = 'ВЫБЕРИТЕ КАТЕГОРИЮ \n'
AMOUNT = 'Сумма: '
DESCRIPTION = 'Описание: '

AMOUNT_VALUE_ERROR = 'Сумма должна быть числом'
DATE_ERROR = 'Формат даты должен быть YYYY-MM-DD'
ACTION_ERROR = 'Неизвестное действие'
CATEGORY_ERROR = 'Неизвестная категория'

ACTION_TYPES_LOC = {
    ActionType.ADD: 'Добавить',
    ActionType.EDIT: 'Отредактировать',
    ActionType.TOTAL: 'Баланс',
    ActionType.SEARCH: 'Поиск',
}

OPERATION_TYPES_LOC = {
    OperationType.INCOME: 'Доход',
    OperationType.EXPENDITURE: 'Расход'
}
