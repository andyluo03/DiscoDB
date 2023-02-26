from flask import Flask, request
import json
import bcrypt
from __main__ import app
from tools import discord_crud
import os
from base64 import b64encode

USERS_CHANNEL_ID = discord_crud.USERS_CHANNEL_ID

@app.route("/setup", methods=["POST"])
def setup():
    # check if channel already exists, if it doesn't return a 409
    channel = discord_crud.get_channel(USERS_CHANNEL_ID)
    if channel.status_code != 200:
        return { "status": 409 }
    
    # add user as admin
    body = json.loads(request.data, strict=False)
    user = body["user"]
    pwd = body["pwd"]
    pwd_hash = bcrypt.hashpw(pwd.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    secret = b64encode(os.urandom(16)).decode("utf-8")
    discord_crud.send_message(USERS_CHANNEL_ID, json.dumps({"user": user, "pwd": pwd_hash, "admin": True, "secret": secret}))
    
    # return success
    return { "status": 200 }