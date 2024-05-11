import json
from datetime import datetime

from personal_wallet.cli import steps
from personal_wallet.settings import WALLET_OPERATION_LOG_PATH, DATE_FORMAT, DBOperationsFields
from personal_wallet.utils import edit_total


def add_operation():
    operation_date = steps.get_date(may_be_empty=True)
    operation = steps.get_operation_type()
    amount = steps.get_amount()
    description = steps.get_description()

    operation_data = {
        DBOperationsFields.DATE.value: operation_date or datetime.now().strftime(DATE_FORMAT),
        DBOperationsFields.OPERATION.value: operation,
        DBOperationsFields.AMOUNT.value: amount,
        DBOperationsFields.DESCRIPTION.value: description,
    }

    with open(WALLET_OPERATION_LOG_PATH, 'r') as f:
        data = json.loads(f.read())

    data['total'] = edit_total(data['total'], amount, operation)

    data['id_count'] += 1
    data['operations'][data['id_count']] = operation_data

    with open(WALLET_OPERATION_LOG_PATH, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
