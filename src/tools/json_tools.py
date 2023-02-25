import json

def verify_json(sample: str) -> bool:
    try:
        json.loads(sample)
    except Exception as e:
        return False
    return True

def match_json(query: dict, message: dict) -> bool:
    if not type(query) is dict:
        return query == message
    for key in query:
        if key not in message:
            return False
        if not match_json(query[key], message[key]):
            return False
    return True