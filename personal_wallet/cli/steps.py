from personal_wallet.localization import USER_DATE, SELECT_OPERATION, AMOUNT, \
    AMOUNT_VALUE_ERROR, DATE_ERROR, DESCRIPTION, OPERATION_TYPES_LOC, CATEGORY_ERROR, \
    EDITED_ACTION_ID, EDITED_ACTION_ID_VALUE_ERROR, AMOUNT_NOT_POSITIVE_ERROR
from personal_wallet.settings import DATE_FORMAT, OperationType
from personal_wallet.utils import date_validator, render_options_list


def get_date(may_be_empty: bool = False,):
    """
    запрашивает у пользователя дату
    :param may_be_empty: Флаг определяет может ли пользователь не вводить дату
    :return: строка с датой введёной пользователем или пустая строка
    """
    while True:
        user_date = input(USER_DATE)
        if user_date == "" and may_be_empty:
            return user_date

        is_date_correct = date_validator(user_date, DATE_FORMAT)
        if is_date_correct:
            return user_date
        else:
            print(DATE_ERROR)


def get_operation_type(may_be_empty: bool = False) -> OperationType | None:
    get_operation_text = SELECT_OPERATION + render_options_list(OPERATION_TYPES_LOC)
    while True:
        operation = input(get_operation_text)
        if operation == "" and may_be_empty:
            return

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


def confirm() -> str:
    return 'да' == input()
