from datetime import datetime
from enum import Enum
from typing import Dict

from personal_wallet.settings import OperationType


def date_validator(date_string: str, date_format: str) -> bool:
    try:
        return bool(datetime.strptime(date_string, date_format))
    except ValueError:
        return False


def render_options_list(localization: Dict[Enum, str]) -> str:
    result = ''
    for key, value in localization.items():
        result += value + ' - ' + key.value + '\n'

    return result


def edit_total(total: float, value: float, operation: OperationType, is_add: bool = True) -> float:
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
        case OperationType.INCOME:
            total += value
        case OperationType.EXPENDITURE:
            total -= value

    return total
