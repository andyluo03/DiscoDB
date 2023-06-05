from flask import Flask, request
import json
import bcrypt
from __main__ import app
from tools import discord, logger, auth
from config import USERS_CHANNEL_ID

@app.route("/new-user", methods=["POST"])
@auth.requires_auth
def new_user(): 
    # get new user info
    try:
        request_body = json.loads(request.data, strict=False)
        name = request_body["name"]
        pwd = request_body["password"]
        assert(type(name) == str and type(pwd) == str)
        assert(len(name) > 0 and len(pwd) > 0)
    except:
        return { "status": "error", "message": "Invalid request body" }, 400
    
    # create new user
    pwd_hash = bcrypt.hashpw(pwd.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    new_user_data = {"name": name, "password": pwd_hash, "admin": True}
    discord.send_message(USERS_CHANNEL_ID, new_user_data)
    
    # below doesnt work bc send_message needs to return the response, we can change that later
    # discord_response = discord_crud.send_message(USERS_CHANNEL_ID, json.dumps(user_data))
    # if discord_response.status_code != 200:
    #     return { "status": "error", "message": "Failed to send message to users channel" }, 500
    
    return { "status": "success", "message": "User created" }, 200