from flask import Flask, request
import requests
import json
from __main__ import app

CONFIG = dict(json.load(open("config.json")))
HEADERS = CONFIG["HEADERS"]
BASE_URL = CONFIG["BASE_URL"]

def match(query, message_content):
    if not type(query) is dict:
        return query == message_content
    for key in query:
        if key not in message_content:
            return False
        
        if not match(query[key], message_content[key]):
            return False
    
    return True   

@app.route("/read")
def read():
    # get data from request
    body = json.loads(request.data, strict=False)
    channel = body["channel"]
    payload = body["data"] # query - { atribute1 : "value1", atribute2 : "value2""}
    parameters = { "limit" : 3 }
    
    matches = {"message_ids": []}
    
    message_list = requests.get(f'{BASE_URL}/channels/{channel}/messages', params=parameters, headers=HEADERS) 
    while len(message_list.json()) != 0:
        # get matches for message_list of max length parameters["limit"] = 100
        for message in message_list.json():
            message_content = json.loads(message["content"])
            if match(payload, message_content):
                matches["message_ids"].append(message["id"]) # append matches to matches list

        # set new message list based on last message of previous message list
        parameters["before"] = message_list.json()[-1]["id"]
        message_list = requests.get(f'{BASE_URL}/channels/{channel}/messages', params=parameters, headers=HEADERS) 

    return matches
    