from flask import Flask, request
import json
from tools import discord_crud, json_tools, logger
from base64 import b64decode
import jwt

from __main__ import app

def validate_user(encoded_token, user_id):
    user_json = json.loads(discord_crud.query_message(discord_crud.USERS_CHANNEL_ID, user_id))
    secret = b64decode(user_json["secret"])
    token = jwt.decode(encoded_token, secret, algorithms=["HS256"])
    return token["user"] == user_json["user"]

@app.route('/messages/', methods=['POST'])
def upload_data():
    logger.log_request(request)

    # Validate user
    encoded_token = request.headers.get('token')
    user_id = request.headers.get('user-id')
    if validate_user(encoded_token, user_id) == False:
        logger.log_failure(403)
        return {"status": 403, "error": "User is not authorized"}
    
    request_body = json.loads(request.data, strict=False)
    target_channel = request_body["channel_id"]
    message_content = request_body["content"]

    if not json_tools.verify_json(message_content):
        logger.log_failure(400)
        return {"status": 400, "error": "JSON is not formatted correctly"}

    discord_crud.send_message(target_channel, message_content)
    
    return {"status": 200}

@app.route('/messages/', methods=['DELETE'])
def delete_data():
    logger.log_request(request)
    
    # Validate user
    encoded_token = request.headers.get('token')
    user_id = request.headers.get('user-id')
    if validate_user(encoded_token, user_id) == False:
        logger.log_failure(403)
        return {"status": 403, "error": "User is not authorized"}

    request_body = json.loads(request.data, strict=False)
    target_channel = request_body["channel_id"]
    message_id = request_body["message_id"]

    discord_crud.delete_message(target_channel, message_id)

    return {"status": 200}

@app.route('/messages/', methods=['GET'])
def query_data():
    logger.log_request(request)
    
    # Validate user
    encoded_token = request.headers.get('token')
    user_id = request.headers.get('user-id')
    if validate_user(encoded_token, user_id) == False:
        logger.log_failure(403)
        return {"status": 403, "error": "User is not authorized"}

    request_body = json.loads(request.data, strict=False)
    target_channel = request_body["channel_id"]
    message_id = request_body["message_id"]

    return discord_crud.query_message(target_channel, message_id)

@app.route('/messages/', methods=['PUT'])
def edit_data():
    logger.log_request(request)
    
    # Validate user
    encoded_token = request.headers.get('token')
    user_id = request.headers.get('user-id')
    if validate_user(encoded_token, user_id) == False:
        logger.log_failure(403)
        return {"status": 403, "error": "User is not authorized"}
    
    request_body = json.loads(request.data, strict=False)
    target_channel = request_body["channel_id"]
    message_id = request_body["message_id"]
    message_content = request_body["content"]

    if not json_tools.verify_json(message_content):
        logger.log_failure(400)
        return {"status": 400, "error": "JSON is not formatted correctly"}

    discord_crud.edit_message(target_channel, message_id, message_content)
    return {"status": 200}