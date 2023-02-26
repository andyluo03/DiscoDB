import requests
import json
from ratelimit import sleep_and_retry, limits

CONFIG = dict(json.load(open("config.json")))
HEADERS = CONFIG["HEADERS"]
BASE_URL = CONFIG["BASE_URL"]
USERS_CHANNEL_ID = CONFIG["USERS_CHANNEL_ID"]

@sleep_and_retry
@limits(calls=5, period=1)
def send_message(channel_id: str, content: str):
    payload = {"content": content}
    requests.post(f'{BASE_URL}/channels/{channel_id}/messages', data=json.dumps(payload), headers=HEADERS)

@sleep_and_retry
@limits(calls=5, period=1)
def delete_message(channel_id: str, message_id: str):
    requests.delete(f'{BASE_URL}/channels/{channel_id}/messages/{message_id}', headers=HEADERS)

@sleep_and_retry
@limits(calls=5, period=1)
def edit_message(channel_id: str, message_id: str, content: str):
    payload = {"content": content}
    requests.patch(f'{BASE_URL}/channels/{channel_id}/messages/{message_id}', data=json.dumps(payload), headers=HEADERS)

@sleep_and_retry
@limits(calls=5, period=1)
def query_message(channel_id: str, message_id: str) -> str:
    data = requests.get(f'{BASE_URL}/channels/{channel_id}/messages/{message_id}', headers=HEADERS)
    return data.json()["content"]

def get_channel(channel_id: str):
    return requests.get(f'{BASE_URL}/channels/{channel_id}', headers=HEADERS)