from requests import get
import json

def repair():
    status = get("https://api.meower.org/status").text
    try:
        load = json.loads(status)
        return load["isRepairMode"]
    except json.decoder.JSONDecodeError:
        pass

def post_id(id):
    home = get("https://api.meower.org/home").text
    post_num = (id - 1)
    try:
        load = json.loads(home)
        return load["index"][id]
    except json.decoder.JSONDecodeError:
        pass

def home():
    home = get("https://api.meower.org/home").text
    try:
        load = json.loads(home)
        return load["index"]
    except json.decoder.JSONDecodeError:
        pass

def home_len():
    home = get("https://api.meower.org/home").text
    try:
        load = json.loads(home)
        return len(load["index"])
    except json.decoder.JSONDecodeError:
        pass

def get_post(id):
    post = get(f"https://api.meower.org/posts?id={id}").text
    try:
        load = json.loads(post)
        return load["u"] + ": " + load["p"]
    except json.decoder.JSONDecodeError:
        pass
