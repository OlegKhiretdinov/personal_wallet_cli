import json
from datetime import datetime

from prettytable import PrettyTable

from personal_wallet.cli.steps import get_search_field, get_search_params
from personal_wallet.localization import OPERATION_TYPES_LOC, INCOME, EXPENSES, TOTAL, OPERATION, \
    DATE, AMOUNT
from personal_wallet.settings import SEARCH_COMMAND, CANCEL_COMMAND, WALLET_OPERATION_LOG_PATH, \
    FilterItemFields, SearchDbFieldsMap, SearchFields, DATE_FORMAT, DBOperationsFields, \
    OperationType, SEARCH_BALANCE_COMMAND

eq_operation = ('=', '!=')
gt_lt_operation = ('<', '>')

# Для каждого элемента SearchFields должны быть определены допустимые операторы
allowed_operator_map = {
    SearchFields.DATE.value: (*eq_operation, *gt_lt_operation),
    SearchFields.AMOUNT.value: (*eq_operation, *gt_lt_operation),
    SearchFields.OPERATION.value: eq_operation
}

search_fn_map = {
    '=': lambda x, y: x == y,
    '!=': lambda x, y: x != y,
    '<': lambda x, y: x < y,
    '>': lambda x, y: x > y
}


def filter_entry(item, filter_list) -> bool:
    """
    Прогоняет запись по списку фильтров
    :param item: запись
    :param filter_list: Список фильтров
    :return:  True если запись соответствует всем фильтрам
    """
    for filter_i in filter_list:
        # поле по которому фильтруем
        field = filter_i[FilterItemFields.FIELD.value]

        # Значение из записи соответствующее полю
        item_val = item[SearchDbFieldsMap[field]]
        # Значение из фильтра
        filter_val = filter_i[FilterItemFields.CONDITION.value]
        # Приведём значения к нужному типу
        match field:
            case SearchFields.AMOUNT.value:
                item_val = float(item_val)
                filter_val = float(filter_val)
            case SearchFields.DATE.value:
                item_val = datetime.strptime(item_val, DATE_FORMAT)
                filter_val = datetime.strptime(filter_val, DATE_FORMAT)

        # Функция соответствующая оператору в фильтре
        filter_fn = search_fn_map[filter_i[FilterItemFields.OPERATOR.value]]

        if not filter_fn(item_val, filter_val):
            return False
    return True


def search():
    filters_list = []
    result = []
    # сбор параметров для поиска
    while True:
        search_filed = get_search_field()

        # в случае ввода неверного значения, повторить запрос
        if not search_filed:
            continue

        # Выход из поиска
        if search_filed == CANCEL_COMMAND:
            return

        # завершение сбора параметров и переход к поиску
        if search_filed == SEARCH_COMMAND or search_filed == SEARCH_BALANCE_COMMAND:
            break

        allowed_operators = allowed_operator_map[search_filed]
        param = get_search_params(search_filed, allowed_operators)

        if not param:
            continue

        operator, condition = param
        filters_list.append({
            FilterItemFields.FIELD.value: search_filed,
            FilterItemFields.OPERATOR.value: operator,
            FilterItemFields.CONDITION.value: condition
        })

    with open(WALLET_OPERATION_LOG_PATH, 'r') as f:
        operations = json.loads(f.read())['operations']

    expenses = 0
    income = 0

    for key, value in operations.items():
        if filter_entry(value, filters_list):
            # Если нужно вывести баланс
            if search_filed == SEARCH_BALANCE_COMMAND:
                if value[DBOperationsFields.OPERATION.value] == OperationType.INCOME.value:
                    income += value[DBOperationsFields.AMOUNT.value]
                else:
                    expenses += value[DBOperationsFields.AMOUNT.value]

            result.append({**value, "id": key})

    entries_table = PrettyTable()

    entries_table.field_names = ['id', DATE, AMOUNT, OPERATION]

    table_rows = []
    for item in result:
        row = [
            item['id'],
            item[DBOperationsFields.DATE.value],
            item[DBOperationsFields.AMOUNT.value],
            OPERATION_TYPES_LOC[item[DBOperationsFields.OPERATION.value]],
        ]
        table_rows.append(row)
    entries_table.add_rows(table_rows)

    print(entries_table)

    # Если нужно вывести баланс по результатам поиска
    if search_filed == SEARCH_BALANCE_COMMAND:
        total_table = PrettyTable()
        total_table.field_names = [INCOME, EXPENSES, TOTAL]
        total_table.add_row([income, expenses, income - expenses])
        print(total_table)
