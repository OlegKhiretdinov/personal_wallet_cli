from datetime import datetime

from personal_wallet.localization import USER_DATE, SELECT_OPERATION, AMOUNT, AMOUNT_VALUE_ERROR, \
    DATE_ERROR, DESCRIPTION, OPERATION_TYPES_LOC, CATEGORY_ERROR, EDITED_ACTION_ID, \
    EDITED_ACTION_ID_VALUE_ERROR, AMOUNT_NOT_POSITIVE_ERROR, SEARCH_FIELDS_LOC, \
    SELECT_SEARCH_FIELD, SEARCH_PARAM_ERROR, INPUT_SEARCH_CONDITION, SEARCH_OPERATION, \
    SEARCH_PARAM_COUNT_ERROR, INVALID_OPERATOR_ERROR
from personal_wallet.settings import DATE_FORMAT, OperationType, CANCEL_COMMAND, SEARCH_COMMAND, \
    SearchFields
from personal_wallet.utils import date_validator, render_options_list, get_all_enum_values


def get_date(may_be_empty: bool = False,):
    """
    запрашивает у пользователя дату
    :param may_be_empty: Флаг определяет может ли пользователь не вводить дату
    :return: строка с датой введёной пользователем или пустая строка
    """
    while True:
        user_date = input(USER_DATE.format(DATE_FORMAT, datetime.now().strftime(DATE_FORMAT)))
        if user_date == "" and may_be_empty:
            return user_date

        if date_validator(user_date, DATE_FORMAT):
            return user_date
        else:
            print(DATE_ERROR.format(DATE_FORMAT, datetime.now().strftime(DATE_FORMAT)))


def get_operation_type(may_be_empty: bool = False) -> OperationType | None:
    get_operation_text = SELECT_OPERATION + render_options_list(OPERATION_TYPES_LOC)
    while True:
        operation = input(get_operation_text)
        if operation == "" and may_be_empty:
            return

        # if operation not in get_all_enum_values(OperationType):
        #     print(CATEGORY_ERROR)
        #     return
        #
        # return operation

        match operation:
            case OperationType.INCOME.value:
                return OperationType.INCOME
            case OperationType.EXPENDITURE.value:
                return OperationType.EXPENDITURE
            case _:
                print(CATEGORY_ERROR)


def get_amount(may_be_empty: bool = False) -> float | None:
    """
    :param may_be_empty: Флаг определяет может ли пользователь ничего не вводить
    :return: число введённое пользователем
    """
    while True:
        amount = input(AMOUNT)
        if amount == "" and may_be_empty:
            return
        try:
            amount = round(float(amount), 2)
            if amount > 0:
                return amount
            print(AMOUNT_NOT_POSITIVE_ERROR)
        except ValueError:
            print(AMOUNT_VALUE_ERROR)


def get_description() -> str:
    return input(DESCRIPTION)


def get_action_id() -> str:
    while True:
        action_id = input(EDITED_ACTION_ID)
        try:
            int(action_id)
            return action_id
        except ValueError:
            print(EDITED_ACTION_ID_VALUE_ERROR)


def get_search_field() -> str | None:
    """
    Запрос у пользователя по какому полю будет идти поиск
    :return: Если введено недопустимое значение возвращает None
    """
    text = SELECT_SEARCH_FIELD + '\n' + render_options_list(SEARCH_FIELDS_LOC)
    search_filed = input(text)

    if search_filed in (*get_all_enum_values(SearchFields), CANCEL_COMMAND, SEARCH_COMMAND):
        return search_filed
    else:
        print(SEARCH_PARAM_ERROR)


def get_search_params(search_filed, allowed_operators) -> list[str] | None:
    """
    Запрашивает и проверяет оператор и значение для поиска
    :param search_filed: поле по которому идёт поиск
    :param allowed_operators: список разрешённых операторов
    :return: список [оператор, значение]. В случае ошибки None
    """
    print(INPUT_SEARCH_CONDITION.format(allowed_operators))
    if search_filed == SearchFields.OPERATION.value:
        print(SEARCH_OPERATION + render_options_list(OPERATION_TYPES_LOC))

    params = input().split()
    # должно быть два параметра разделённых пробелом
    if len(params) != 2:
        print(SEARCH_PARAM_COUNT_ERROR.format(2))
        return

    operator, value = params
    # для некоторых полей есть ограничение на использование операторов
    if operator not in allowed_operators:
        print(INVALID_OPERATOR_ERROR.format(operator))
        return
    # Проверка соответствия значении полю, по которому идёт поиск
    match search_filed:
        case SearchFields.DATE.value:
            if not date_validator(value, DATE_FORMAT):
                print(DATE_ERROR.format(DATE_FORMAT, datetime.now().strftime(DATE_FORMAT)))
                return
        case SearchFields.AMOUNT.value:
            try:
                float(value)
            except ValueError:
                print(AMOUNT_VALUE_ERROR)
                return
        case SearchFields.OPERATION.value:
            if value not in get_all_enum_values(OperationType):
                print(SEARCH_PARAM_ERROR)
                return

    return params
