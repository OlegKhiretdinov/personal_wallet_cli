import json

from personal_wallet.cli import steps
from personal_wallet.settings import WALLET_OPERATION_LOG_PATH, OperationType


def add_operation():
    operation_date = steps.get_date()
    category = steps.get_category()
    amount = steps.get_amount()
    description = steps.get_description()

    operation_data = {
        'date': operation_date,
        'category': category.name,
        'amount': amount,
        'description': description,
    }

    with open(WALLET_OPERATION_LOG_PATH, 'r') as f:
        data = json.loads(f.read())

    match category:
        case OperationType.INCOME:
            data['total'] += amount
        case OperationType.EXPENDITURE:
            data['total'] -= amount

    data['id_count'] += 1
    operation_data['id'] = data['id_count']
    data['operations'].append(operation_data)

    with open(WALLET_OPERATION_LOG_PATH, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
