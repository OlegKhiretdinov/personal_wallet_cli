from personal_wallet.settings import ActionType, OperationType, SearchFields

WELCOME_TEXT = 'Personal Wallet v 0.1.0'
SELECT_ACTON = 'ВЫБЕРИТЕ ДЕЙСТВИЕ \n'
USER_DATE = 'Введите дату в формате {}. Пример: {}\n'
SELECT_OPERATION = 'ВЫБЕРИТЕ ОПЕРАЦИЮ \n'
AMOUNT = 'Сумма'
DESCRIPTION = 'Описание: '
EDITED_ACTION_ID = 'ID редактируемого действия: '
SELECT_SEARCH_FIELD = 'Выберите по какому полю будет идти поиск:'
INPUT_SEARCH_CONDITION = 'Введите условия поиска\nСписок доступных операторов {} '
SEARCH_OPERATION = 'В качестве параметра поиска выберите номер операции из списк\n'
INCOME = "Доход"
EXPENSES = "Расход"
TOTAL = "Итого"
DATE = 'Дата'
OPERATION = 'Операция'
BALANCE = 'Баланс'

ACTION_ID_NOT_FOUND = 'Запись с ID = {} не найдена'
AMOUNT_VALUE_ERROR = 'Сумма должна быть числом'
AMOUNT_NOT_POSITIVE_ERROR = 'Сумма должна быть положительным числом'
EDITED_ACTION_ID_VALUE_ERROR = 'ID должен быть целым числом'
DATE_ERROR = 'Формат даты должен быть  {}. Пример: {}'
ACTION_ERROR = 'Неизвестное действие'
CATEGORY_ERROR = 'Неизвестная категория'
SEARCH_PARAM_ERROR = 'Не верный параметр поиска'
SEARCH_PARAM_COUNT_ERROR = 'Для поиска необходимое колличество параметров: {} '
INVALID_OPERATOR_ERROR = 'Недопустимый оператор: {}'
INVALID_CONDITION_FORMAT_ERROR = 'Не верный формат условия: {}'

ACTION_TYPES_LOC = {
    ActionType.ADD.value: 'Добавить',
    ActionType.EDIT.value: 'Отредактировать',
    ActionType.TOTAL.value: 'Баланс',
    ActionType.SEARCH.value: 'Поиск',
}

OPERATION_TYPES_LOC = {
    OperationType.INCOME.value: INCOME,
    OperationType.EXPENDITURE.value: EXPENSES
}

SEARCH_FIELDS_LOC = {
    SearchFields.DATE.value: 'дата',
    SearchFields.AMOUNT.value: 'сумма',
    SearchFields.OPERATION.value: 'тип операции'
}
