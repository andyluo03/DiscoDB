from flask import Flask, request
import requests
import json
from __main__ import app

CONFIG = dict(json.load(open("config.json")))
HEADERS = CONFIG["HEADERS"]
BASE_URL = CONFIG["BASE_URL"]

@app.route("/update")
def update():
    body = json.loads(request.data, strict=False)
    channel = body["channel"]
    message_id = body["message_id"]
    payload = body["data"]

    x = requests.patch(f'{BASE_URL}/channels/{channel}/messages/{message_id}', data=json.dumps(payload), headers=HEADERS)
    print(x)

    return "Success!"