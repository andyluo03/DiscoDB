import requests
import json

CONFIG = dict(json.load(open("config.json")))
HEADERS = CONFIG["HEADERS"]
BASE_URL = CONFIG["BASE_URL"]

def send_message(channel_id: str, content: str):
    payload = {"content": content}
    requests.post(f'{BASE_URL}/channels/{channel_id}/messages', data=json.dumps(payload), headers=HEADERS)

def delete_message(channel_id: str, message_id: str):
    requests.delete(f'{BASE_URL}/channels/{channel_id}/messages/{message_id}', headers=HEADERS)

def edit_message(channel_id: str, message_id: str, content: str):
    payload = {"content": content}
    requests.patch(f'{BASE_URL}/channels/{channel_id}/messages/{message_id}', data=json.dumps(payload), headers=HEADERS)

def query_message(channel_id: str, message_id: str) -> str:
    data = requests.get(f'{BASE_URL}/channels/{channel_id}/messages/{message_id}', headers=HEADERS)
    return data.json()["content"]