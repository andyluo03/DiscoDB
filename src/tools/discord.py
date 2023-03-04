import requests
import json
from ratelimit import sleep_and_retry, limits

CONFIG = dict(json.load(open("config.json")))
HEADERS = CONFIG["HEADERS"]
BASE_URL = CONFIG["BASE_URL"]
USERS_CHANNEL_ID = CONFIG["USERS_CHANNEL_ID"]

#Block function execution until done
@sleep_and_retry
@limits(calls=40, period=1)
def unified_ratelimiter():
    return True

def send_message(channel_id: str, content: dict) -> dict:
    unified_ratelimiter()
    payload = {"content": json.dumps(content)}
    res=requests.post(f'{BASE_URL}/channels/{channel_id}/messages', data=json.dumps(payload), headers=HEADERS)
    return res.json()

def delete_message(channel_id: str, message_id: str) -> None:
    unified_ratelimiter()
    res=requests.delete(f'{BASE_URL}/channels/{channel_id}/messages/{message_id}', headers=HEADERS)

def edit_message(channel_id: str, message_id: str, content: dict) -> dict:
    unified_ratelimiter()
    payload = {"content": json.dumps(content)}
    res=requests.patch(f'{BASE_URL}/channels/{channel_id}/messages/{message_id}', data=json.dumps(payload), headers=HEADERS)
    return res.json()

def query_message(channel_id: str, message_id: str) -> dict:
    unified_ratelimiter()
    data = requests.get(f'{BASE_URL}/channels/{channel_id}/messages/{message_id}', headers=HEADERS)
    return json.loads(data.json()["content"])

def get_channel(channel_id: str) -> requests.Response:
    unified_ratelimiter()
    return requests.get(f'{BASE_URL}/channels/{channel_id}', headers=HEADERS)
