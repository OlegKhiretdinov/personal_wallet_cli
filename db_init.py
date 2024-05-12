import pathlib
import json

from personal_wallet.settings import WALLET_OPERATION_LOG_PATH

p = pathlib.PurePath(WALLET_OPERATION_LOG_PATH)
db_path = p.parents[0]
empty_bd = {
  "id_count": 0,
  "total": 0,
  "operations": {}
}

if not pathlib.Path(db_path).exists():
    pathlib.Path(db_path).mkdir()
    with open(WALLET_OPERATION_LOG_PATH, "w+") as db:
        json.dump(empty_bd, db, indent=2)
