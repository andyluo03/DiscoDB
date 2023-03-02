from flask import Flask, request
import json
import bcrypt
import jwt
import requests
from base64 import b64decode
from ratelimit import sleep_and_retry, limits

from __main__ import app
from tools import discord_crud

CONFIG = dict(json.load(open("config.json")))
HEADERS = CONFIG["HEADERS"]
BASE_URL = CONFIG["BASE_URL"]
USERS_CHANNEL_ID = CONFIG["USERS_CHANNEL_ID"]
SECRET_KEY = CONFIG["SECRET_KEY"]

@sleep_and_retry
@limits(calls=2, period=1)
def query_user(name: str):
    parameters = {"limit":100}
    message_list = requests.get(f'{BASE_URL}/channels/{USERS_CHANNEL_ID}/messages', params=parameters, headers=HEADERS)
    # iterate through messages until user is found
    while len(message_list.json()) != 0:
        for message in message_list.json():
            message_content = json.loads(message["content"])
            message_id = message["id"]
            if message_content["name"] == name:
                return message_content, message_id # user_json, user_id
        parameters["before"] = message_list.json()[-1]["id"]
        message_list = requests.get(f'{BASE_URL}/channels/{USERS_CHANNEL_ID}/messages', params=parameters, headers=HEADERS) 
    return None, None

@app.route("/login", methods=["PUT"])
def login():
    # get username and pwd from request body
    try:
        request_body = json.loads(request.data, strict=False)
        name = request_body["name"]
        pwd = request_body["password"]
        assert(type(name) == str and type(pwd) == str)
        assert(len(name) > 0 and len(pwd) > 0)
    except:
        return { "status" : "error", "message" : "Invalid request body" }, 400
    
    # check if user exists
    user_json, user_id = query_user(name)
    if not user_json:
        return { "status" : "error", "message" : "User not found" }, 404
    
    # check if password is correct
    if (bcrypt.checkpw(pwd.encode("utf-8"), user_json["password"].encode("utf-8")) == False):
        return { "status" : "error", "message" : "Incorrect password" }, 403
    
    # generate token
    token = jwt.encode({"sub": user_id, "name": name, "admin": user_json["admin"]}, SECRET_KEY, algorithm="HS256")
    
    return { "Authorization" : "Bearer " + token, "status" : "success", "message" : "User logged in" }, 200