import json
from datetime import datetime

from personal_wallet.cli.steps import get_search_field, get_search_params
from personal_wallet.settings import SEARCH_COMMAND, CANCEL_COMMAND, WALLET_OPERATION_LOG_PATH, \
    FilterItemFields, SearchDbFieldsMap, SearchFields, DATE_FORMAT

eq_operation = ('=', '!=')
gt_lt_operation = ('<', '>')

# Для каждого элемента SearchFields должны быть определены разрешённые операторы
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


def filter_entrie(item, filter_list) -> bool:
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
        if search_filed == SEARCH_COMMAND:
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

    for key, value in operations.items():
        if filter_entrie(value, filters_list):
            result.append({**value, "id": key})
    print("SEARCH", result)
