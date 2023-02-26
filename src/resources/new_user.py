from flask import Flask, request
import json
import bcrypt
import jwt
from __main__ import app
from tools import discord_crud, logger
import os
from base64 import b64encode, b64decode
import requests

BASE_URL = discord_crud.BASE_URL
HEADERS = discord_crud.HEADERS
USERS_CHANNEL_ID = discord_crud.USERS_CHANNEL_ID

def validate_user(encoded_token, user_id):
    user_json = json.loads(discord_crud.query_message(discord_crud.USERS_CHANNEL_ID, user_id))
    secret = b64decode(user_json["secret"])
    token = jwt.decode(encoded_token, secret, algorithms=["HS256"])
    return token["user"] == user_json["user"]

@app.route("/new_user", methods=["POST"])
def new_user():
     # Validate user
    encoded_token = request.headers.get('token')
    user_id = request.headers.get('user-id')
    if validate_user(encoded_token, user_id) == False:
        logger.log_failure(403)
        return {"status": 403, "error": "User is not authorized"}
    
    body = json.loads(request.data, strict=False)
    # add user
    new_user = body["new_user"]
    new_pwd = body["new_pwd"]
    pwd_hash = bcrypt.hashpw(new_pwd.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    new_secret = b64encode(os.urandom(16)).decode("utf-8")
    discord_crud.send_message(USERS_CHANNEL_ID, json.dumps({"user": new_user, "pwd": pwd_hash, "admin": True, "secret": new_secret}))
    
    return { "status": 200 }