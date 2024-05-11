from datetime import datetime
from typing import Dict

from personal_wallet.settings import OperationType


def date_validator(date_string: str, date_format: str) -> bool:
    try:
        return bool(datetime.strptime(date_string, date_format))
    except ValueError:
        return False


def render_options_list(localization: Dict[str, str]) -> str:
    result = ''
    for key, value in localization.items():
        result += f'{key} - {value}\n'

    return result


def edit_total(total: float, value: float, operation: str, is_add: bool = True) -> float:
    """
    Изменение итоговой суммы при добавлении или удалении записи
    :param total: начальная сумма
    :param value: величина на которую изменятся
    :param operation: тип операции (доход или расход)
    :param is_add: флаг определяющи добавляется или удаляется запись
    :return: итоговая сумма
    """
    if not is_add:
        value = -value

    match operation:
        case OperationType.INCOME.value:
            total += value
        case OperationType.EXPENDITURE.value:
            total -= value

    return total


def get_all_enum_values(enum) -> list[str]:
    """
    Возвращает список значений енума
    :param enum: Enum
    :return: list
    """
    return [e.value for e in enum]
