from datetime import datetime

from personal_wallet.localization import USER_DATE, INSERT_DATA_DEFAULT, \
    SELECT_CATEGORY, AMOUNT, AMOUNT_VALUE_ERROR, DATE_ERROR, DESCRIPTION, \
    OPERATION_TYPES_LOC, CATEGORY_ERROR
from personal_wallet.settings import DATE_FORMAT, OperationType
from personal_wallet.utils import date_validator, render_options_list


def get_date():
    while True:
        user_date = input(f'{USER_DATE}\n{INSERT_DATA_DEFAULT}')
        if user_date == "":
            return datetime.now().strftime(DATE_FORMAT)

        is_date_correct = date_validator(user_date, DATE_FORMAT)
        if is_date_correct:
            return user_date
        else:
            print(DATE_ERROR)


def get_category() -> OperationType:
    get_cat_text = SELECT_CATEGORY + render_options_list(OPERATION_TYPES_LOC)
    while True:
        category = input(get_cat_text)
        match category:
            case OperationType.INCOME.value:
                return OperationType.INCOME
            case OperationType.EXPENDITURE.value:
                return OperationType.EXPENDITURE
            case _:
                print(CATEGORY_ERROR)


def get_amount() -> float:
    while True:
        amount = input(AMOUNT)
        try:
            return round(float(amount), 2)
        except ValueError:
            print(AMOUNT_VALUE_ERROR)


def get_description() -> str:
    return input(DESCRIPTION)


def confirm() -> str:
    return 'да' == input()
