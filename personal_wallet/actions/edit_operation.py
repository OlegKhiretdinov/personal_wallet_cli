import json

from personal_wallet.cli import steps
from personal_wallet.settings import WALLET_OPERATION_LOG_PATH, OperationType, DBOperationsFields
from personal_wallet.localization import ACTION_ID_NOT_FOUND
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
        return

    operation_date = steps.get_date(may_be_empty=True)
    operation = steps.get_operation_type(may_be_empty=True) or editable_entry["operation"]
    amount = steps.get_amount(may_be_empty=True)
    description = steps.get_description()

    new_raw_data = {
        DBOperationsFields.DATE.value: operation_date,
        DBOperationsFields.OPERATION.value: operation,
        DBOperationsFields.AMOUNT.value: amount,
        DBOperationsFields.DESCRIPTION.value: description,
    }

    new_data = dict((item for item in new_raw_data.items() if item[1]))

    data['total'] = edit_total(
        data['total'],
        editable_entry['amount'],
        editable_entry['operation'],
        False
    )

    editable_entry.update(new_data)

    data['total'] = edit_total(data['total'], editable_entry['amount'], operation)

    with open(WALLET_OPERATION_LOG_PATH, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
