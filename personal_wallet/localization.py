from personal_wallet.settings import ActionType, OperationType

WELCOME_TEXT = 'Personal Wallet v 0.1.0'
SELECT_ACTON = 'ВЫБЕРИТЕ ДЕЙСТВИЕ \n'
USER_DATE = 'Введите дату в формате YYYY-MM-DD'
INSERT_DATE_DEFAULT = 'Если оставить пустым подставится текущая дата: '
UPDATE_DATE_DEFAULT = 'Если оставить пустым, дата не изменится: '
SELECT_OPERATION = 'ВЫБЕРИТЕ ОПЕРАЦИЮ \n'
AMOUNT = 'Сумма: '
DESCRIPTION = 'Описание: '
EDITED_ACTION_ID = 'ID редактируемого действия: '

ACTION_ID_NOT_FOUND = 'Запись с ID = {} не найдена'
AMOUNT_VALUE_ERROR = 'Сумма должна быть числом'
AMOUNT_NOT_POSITIVE_ERROR = 'Сумма должна быть положительным числом'
EDITED_ACTION_ID_VALUE_ERROR = 'ID должен быть целым числом'
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
