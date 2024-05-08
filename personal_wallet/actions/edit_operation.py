import json

from personal_wallet.cli import steps
from personal_wallet.settings import WALLET_OPERATION_LOG_PATH, OperationType
from personal_wallet.localization import ACTION_ID_NOT_FOUND, UPDATE_DATE_DEFAULT
from personal_wallet.utils import edit_total


def edit_operation():
    action_id = steps.get_action_id()

    with open(WALLET_OPERATION_LOG_PATH, 'r') as f:
        data = json.loads(f.read())

    try:
        editable_entry = data['operations'][action_id]
        print(editable_entry)
    except KeyError:
        print(ACTION_ID_NOT_FOUND.format(action_id))

    operation_date = steps.get_date(may_be_empty=True, default_text=UPDATE_DATE_DEFAULT)
    operation = steps.get_operation_type()
    amount = steps.get_amount(True)
    description = steps.get_description()

    operation_new_raw_data = {
        'date': operation_date,
        'operation': operation.name,
        'amount': amount,
        'description': description,
    }

    operation_new_data = dict((item for item in operation_new_raw_data.items() if item[1]))

    data['total'] = edit_total(
        data['total'],
        editable_entry['amount'],
        OperationType[editable_entry['operation']],
        False
    )

    editable_entry.update(operation_new_data)

    data['total'] = edit_total(data['total'], editable_entry['amount'], operation)

    with open(WALLET_OPERATION_LOG_PATH, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
