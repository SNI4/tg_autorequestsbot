import json
from data.config import ADMIN_ID, ADMIN_USERNAME


async def add_admin(user_id: str, username: str) -> bool | str:
    try:
        with open('data/admins.json', 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data[user_id] = username
            f.seek(0)
            json.dump(data, f)
            f.truncate()
            return True
    except Exception as e:
        return str(e)


async def del_admin(user_id: str) -> bool | str:
    try:
        with open('data/admins.json', 'r+', encoding='utf-8') as f:
            data = json.load(f)
            del data[user_id]
            f.seek(0)
            json.dump(data, f)
            f.truncate()
            return True
    except Exception as e:
        return str(e)


async def get_admins() -> dict | str:
    try:
        with open('data/admins.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            data[ADMIN_ID] = ADMIN_USERNAME
            return data
    except Exception as e:
        return str(e)
