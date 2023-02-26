import requests
import time
import json
from ratelimit import sleep_and_retry, limits

CONFIG = dict(json.load(open("config.json")))
HEADERS = CONFIG["HEADERS"]
BASE_URL = CONFIG["BASE_URL"]
LOG_CHANNEL = CONFIG["LOG_CHANNEL_ID"]

@sleep_and_retry
@limits(calls=5, period=1)
def log_request(unprocessed_request):
    log = {"content": '{"type": "' + unprocessed_request.method + '", "time": "' + str(time.time()) + '"}'}
    requests.post(f'{BASE_URL}/channels/{LOG_CHANNEL}/messages', data=json.dumps(log),headers=HEADERS)

@sleep_and_retry
@limits(calls=5, period=1)
def log_failure(status_code):
    log = {"content": '{"error": "'+ status_code +'", "time": "' + str(time.time()) + '"}'}
    requests.post(f'{BASE_URL}/channels/{LOG_CHANNEL}/messages', data=json.dumps(log),headers=HEADERS)