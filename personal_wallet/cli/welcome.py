from personal_wallet.actions import add_operation
from personal_wallet.localization import WELCOME_TEXT, SELECT_ACTON, \
    ACTION_ERROR, ACTION_TYPES_LOC
from personal_wallet.settings import ActionType
from personal_wallet.utils import render_options_list


def welcome():
    print(WELCOME_TEXT)
    action_text = SELECT_ACTON + render_options_list(ACTION_TYPES_LOC)
    while (action := input(action_text)) != 'q':
        match action:
            case ActionType.ADD.value:
                add_operation.add_operation()
            case _:
                print(ACTION_ERROR)
