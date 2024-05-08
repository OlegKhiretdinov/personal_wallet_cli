from datetime import datetime
from typing import Dict
from enum import Enum


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
