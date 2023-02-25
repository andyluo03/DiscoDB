from flask import Flask, request
import requests
import json
from __main__ import app

CONFIG = dict(json.load(open("config.json")))
HEADERS = CONFIG["HEADERS"]
BASE_URL = CONFIG["BASE_URL"]

@app.route("/create")
def create():
    body = json.loads(request.data, strict=False)
    channel = body["channel"]
    payload = body["data"]

    x = requests.post(f'{BASE_URL}/channels/{channel}/messages', data=json.dumps(payload), headers=HEADERS)
    print(x.text)

    return "Success!"