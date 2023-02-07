import json


async def get_channels() -> str | dict:
    try:
        with open('data/channels.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(e)
        return str(e)


async def add_approved(channel_id: str) -> bool | str:
    try:
        with open('data/channels.json', 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data[channel_id]["users"] += 1
            f.seek(0)
            json.dump(data, f)
            f.truncate()
            return True

    except Exception as e:
        print(e)
        return str(e)


async def add_channel(channel_id: str, channel_name: str) -> bool | str:
    with open('data/channels.json', 'r+', encoding='utf-8') as f:
        data = json.load(f)
        if channel_id not in data.keys():
            data[channel_id] = {"channel_name": channel_name, "users": 0}
            f.seek(0)
            json.dump(data, f)
            f.truncate()
            return True
        else:
            return "Такой канал уже существует!"


async def del_channel(channel_id: str) -> bool:
    try:
        with open('data/channels.json', 'r+', encoding='utf-8') as f:
            data = json.load(f)
            del data[channel_id]
            f.seek(0)
            json.dump(data, f)
            f.truncate()
            return True
    except KeyError:
        return False
