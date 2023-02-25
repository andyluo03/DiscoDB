import requests
import json

CONFIG = dict(json.load(open("config.json")))
HEADERS = CONFIG["HEADERS"]
BASE_URL = CONFIG["BASE_URL"]
LOG_CHANNEL = CONFIG["LOG_CHANNEL"]

def log_request(unprocessed_request):
    log = {"content": '{"type": "' + unprocessed_request.method + '"}'}
    requests.post(f'{BASE_URL}/channels/{LOG_CHANNEL}/messages', data=json.dumps(log),headers=HEADERS)

def log_failure(status_code):
    log = {"content": '{"error": "'+ status_code +'"}'}
    requests.post(f'{BASE_URL}/channels/{LOG_CHANNEL}/messages', data=json.dumps(log),headers=HEADERS)