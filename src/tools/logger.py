import requests
import time
import json

CONFIG = dict(json.load(open("config.json")))
HEADERS = CONFIG["HEADERS"]
BASE_URL = CONFIG["BASE_URL"]
LOG_CHANNEL = CONFIG["LOG_CHANNEL_ID"]

def log_request(unprocessed_request):
    log = {"content": '{"type": "' + unprocessed_request.method + '", "time": "' + str(time.time()) + '"}'}
    requests.post(f'{BASE_URL}/channels/{LOG_CHANNEL}/messages', data=json.dumps(log),headers=HEADERS)

def log_failure(status_code):
    log = {"content": '{"error": "'+ status_code +'", "time": "' + str(time.time()) + '"}'}
    requests.post(f'{BASE_URL}/channels/{LOG_CHANNEL}/messages', data=json.dumps(log),headers=HEADERS)