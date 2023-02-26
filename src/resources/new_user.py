from flask import Flask, request
import json
import bcrypt
import jwt
from __main__ import app
from tools import discord_crud
import os
from base64 import b64encode, b64decode
import requests

BASE_URL = discord_crud.BASE_URL
HEADERS = discord_crud.HEADERS
USERS_CHANNEL_ID = discord_crud.USERS_CHANNEL_ID

def query_user(user: str):
    parameters = {"limit":100}
    message_list = requests.get(f'{BASE_URL}/channels/{USERS_CHANNEL_ID}/messages', params=parameters, headers=HEADERS)
    while len(message_list.json()) != 0:
        for message in message_list.json():
            user_content = json.loads(message["content"])
            if user_content["user"] == user:
                return user_content
        parameters["before"] = message_list.json()[-1]["id"]
        message_list = requests.get(f'{BASE_URL}/channels/{USERS_CHANNEL_ID}/messages', params=parameters, headers=HEADERS) 
    return None

@app.route("/new_user", methods=["POST"])
def new_user():
    # get encoded token
    encoded_token = request.headers.get('token')
    if encoded_token is None:
        return { "status": 418 }
    
    # get user json
    body = json.loads(request.data, strict=False)
    user = body["user"]
    user_json = query_user(user)
    if user_json is None:
        return { "status": 400 }
    if user_json["admin"] == False:
        return { "status": 401 }
    
    # validate user
    secret = b64decode(user_json["secret"])
    token = jwt.decode(encoded_token, secret, algorithms=["HS256"])
    if token["user"] != user:
        return { "status": 402 }
    
    # add user
    new_user = body["new_user"]
    new_pwd = body["new_pwd"]
    pwd_hash = bcrypt.hashpw(new_pwd.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    new_secret = b64encode(os.urandom(16)).decode("utf-8")
    discord_crud.send_message(USERS_CHANNEL_ID, json.dumps({"user": new_user, "pwd": pwd_hash, "admin": True, "secret": new_secret}))
    
    return { "status": 200 }