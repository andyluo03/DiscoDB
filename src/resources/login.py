from flask import Flask, request
import json
import bcrypt
import jwt
from __main__ import app
from tools import discord_crud
import requests
from base64 import b64decode

BASE_URL = discord_crud.BASE_URL
HEADERS = discord_crud.HEADERS
USERS_CHANNEL_ID = discord_crud.USERS_CHANNEL_ID

def query_user(user: str):
    parameters = {"limit":100}
    user_list = requests.get(f'{BASE_URL}/channels/{USERS_CHANNEL_ID}/messages', params=parameters, headers=HEADERS)
    while len(message_list.json()) != 0:
        for user in user_list.json():
            user_content = json.loads(user["content"])
            if user_content["user"] == user:
                return user_content
        parameters["before"] = message_list.json()[-1]["id"]
        message_list = requests.get(f'{BASE_URL}/channels/{USERS_CHANNEL_ID}/messages', params=parameters, headers=HEADERS) 
    return None

@app.route("/login", methods=["PUT"])
def login():
    body = json.loads(request.data, strict=False)
    user = body["user"]
    pwd = body["pwd"]
    
    if user is None or pwd is None:
        return { "status": 400 }
    
    user_match = query_user(user)
    if user_match is None:
        return { "status": 404 }
    
    if (bcrypt.checkpw(pwd.encode("utf-8"), user_match["pwd"].encode("utf-8")) == False):
        return { "status": 401 }
    
    secret = user_match["secret"]
    if secret is None:
        return { "status": 403 }
    
    token = jwt.encode({"user": user, "admin": user_match["admin"]}, b64decode(secret), algorithm="HS256")
    print(token)
    return token