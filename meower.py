from requests import get
import json

def repair():
    status = get("https://api.meower.org/status").text
    try:
        load = json.loads(status)
        return load["isRepairMode"]
    except json.decoder.JSONDecodeError:
        return False

def post_id(post):
    home = get("https://api.meower.org/home").text
    try:
        load = json.loads(home)
        return load["index"][post]
    except json.decoder.JSONDecodeError:
        pass
