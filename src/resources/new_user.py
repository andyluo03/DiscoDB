from flask import Flask, request
import json
import bcrypt
import jwt
from __main__ import app
from tools import discord, logger, auth

CONFIG = dict(json.load(open("config.json")))
HEADERS = CONFIG["HEADERS"]
BASE_URL = CONFIG["BASE_URL"]
USERS_CHANNEL_ID = CONFIG["USERS_CHANNEL_ID"]
SECRET_KEY = CONFIG["SECRET_KEY"]

# def validate_user(encoded_token, user_id):
#     user_json = json.loads(discord_crud.query_message(USERS_CHANNEL_ID, user_id))
#     secret = b64decode(user_json["secret"])
#     token = jwt.decode(encoded_token, secret, algorithms=["HS256"])
#     return token["user"] == user_json["user"]

# type param as list of str
# def is_authorized(auth_header) -> bool:
#     try:
#         auth_header_split = auth_header.split(" ")
#         assert(len(auth_header_split) == 2 and auth_header_split[0] == "Bearer") # check if auth header is valid
#         encoded_token = auth_header_split[1]
#         token = jwt.decode(encoded_token, SECRET_KEY, algorithms=["HS256"]) # check if token is valid
#         assert(token["admin"] == True) # check if user is admin in token
#         user_json = discord.query_message(USERS_CHANNEL_ID, token["sub"])
#         assert(user_json["admin"] == True) # check if user is admin in db
#         assert(user_json["name"] == token["name"]) # check if user name in db matches name in token
#         return True
#     except:
#         return False

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