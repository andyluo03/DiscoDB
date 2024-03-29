from flask import Flask, request
import json
import requests
from ratelimit import sleep_and_retry, limits
from tools import discord, json_tools, logger, auth
from __main__ import app
from config import BASE_URL, HEADERS

@sleep_and_retry
@limits(calls=2,period=1)
def get_matches(channel_id: str, attributes: dict):
    matches = {"message_ids": []}
    parameters = {"limit":100}
    message_list = requests.get(f'{BASE_URL}/channels/{channel_id}/messages', params=parameters, headers=HEADERS)
    while len(message_list.json()) != 0:
        for message in message_list.json():
            message_content = json.loads(message["content"])
            if json_tools.match_json(attributes, message_content):
                matches["message_ids"].append(message["id"])

        parameters["before"] = message_list.json()[-1]["id"]
        message_list = requests.get(f'{BASE_URL}/channels/{channel_id}/messages', params=parameters, headers=HEADERS) 

    return matches


@app.route('/query/', methods=['GET'])
@auth.requires_auth
def query(): 
    request_body = json.loads(request.data, strict=False)
    target_channel = request_body["channel_id"]
    attributes = request_body["attributes"]

    matches = get_matches(target_channel, attributes)

    return matches, 200