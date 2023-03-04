from flask import Flask, request
import json
from tools import discord, logger, auth
from base64 import b64decode
import jwt

from __main__ import app

@app.route('/messages/', methods=['POST'])
def upload_data():
    logger.log_request(request)

    # authorize user
    auth_header = request.headers.get('Authorization')
    if not auth.is_authorized(auth_header):
        return { "status" : "error", "message": "User is not authorized"}, 403
    
    request_body = json.loads(request.data, strict=False)
    target_channel = request_body["channel_id"]
    message_content = request_body["content"]

    discord.send_message(target_channel, message_content)
    
    return {"status": 200}

@app.route('/messages/', methods=['DELETE'])
def delete_data():
    logger.log_request(request)
    
    # authorize user
    auth_header = request.headers.get('Authorization')
    if not auth.is_authorized(auth_header):
        return { "status" : "error", "message": "User is not authorized"}, 403

    request_body = json.loads(request.data, strict=False)
    target_channel = request_body["channel_id"]
    message_id = request_body["message_id"]

    discord.delete_message(target_channel, message_id)

    return {"status": 200}

@app.route('/messages/', methods=['GET'])
def query_data():
    logger.log_request(request)
    
    # authorize user
    auth_header = request.headers.get('Authorization')
    if not auth.is_authorized(auth_header):
        return { "status" : "error", "message": "User is not authorized"}, 403

    request_body = json.loads(request.data, strict=False)
    target_channel = request_body["channel_id"]
    message_id = request_body["message_id"]

    return discord.query_message(target_channel, message_id)

@app.route('/messages/', methods=['PUT'])
def edit_data():
    logger.log_request(request)
    
    # authorize user
    auth_header = request.headers.get('Authorization')
    if not auth.is_authorized(auth_header):
        return { "status" : "error", "message": "User is not authorized"}, 403
    
    request_body = json.loads(request.data, strict=False)
    target_channel = request_body["channel_id"]
    message_id = request_body["message_id"]
    message_content = request_body["content"]

    discord.edit_message(target_channel, message_id, message_content)
    return {"status": 200}