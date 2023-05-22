import json
from . import discord
import jwt
from flask import request
from config import USERS_CHANNEL_ID, SECRET_KEY

def requires_auth(f):
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        try:
            assert(auth_header is not None)
            auth_header_split = auth_header.split(' ')
            # check if auth header is valid
            assert(len(auth_header_split) == 2 and auth_header_split[0] == "Bearer")
            # check if token is valid
            encoded_token = auth_header_split[1]
            token = jwt.decode(encoded_token, SECRET_KEY, algorithms=["HS256"])
            # check if user is admin in token
            assert(token["admin"] == True)
            # check if user is admin in db and if user name in db matches name in token
            user_json = discord.query_message(USERS_CHANNEL_ID, token["sub"])
            assert(user_json["admin"] == True)
            assert(user_json["name"] == token["name"])
            
        except:
            return { "status": "error", "message": "User is not authorized" }, 403
        return f(*args, **kwargs)
    decorated.__name__ = f.__name__
    return decorated