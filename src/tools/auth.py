import json
from . import discord
import jwt

CONFIG = dict(json.load(open("config.json")))
HEADERS = CONFIG["HEADERS"]
BASE_URL = CONFIG["BASE_URL"]
USERS_CHANNEL_ID = CONFIG["USERS_CHANNEL_ID"]
SECRET_KEY = CONFIG["SECRET_KEY"]

def is_authorized(auth_header) -> bool:
    try:
        auth_header_split = auth_header.split(' ')
        assert(len(auth_header_split) == 2 and auth_header_split[0] == "Bearer") # check if auth header is valid
        encoded_token = auth_header_split[1]
        token = jwt.decode(encoded_token, SECRET_KEY, algorithms=["HS256"]) # check if token is valid
        assert(token["admin"] == True) # check if user is admin in token
        user_json = discord.query_message(USERS_CHANNEL_ID, token["sub"])
        assert(user_json["admin"] == True) # check if user is admin in db
        assert(user_json["name"] == token["name"]) # check if user name in db matches name in token
        return True
    except:
        return False