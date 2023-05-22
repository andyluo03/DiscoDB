from flask import Flask, request
import json
from tools import discord, logger, auth

from __main__ import app

@app.route('/messages/', methods=['POST'])
@auth.requires_auth
def upload_data():
    logger.log_request(request)
    
    request_body = json.loads(request.data, strict=False)
    target_channel = request_body["channel_id"]
    message_content = request_body["content"]

    discord.send_message(target_channel, message_content)
    
    return {"status": 200}

@app.route('/messages/', methods=['DELETE'])
@auth.requires_auth
def delete_data():
    logger.log_request(request)

    request_body = json.loads(request.data, strict=False)
    target_channel = request_body["channel_id"]
    message_id = request_body["message_id"]

    discord.delete_message(target_channel, message_id)

    return {"status": 200}

@app.route('/messages/', methods=['GET'])
@auth.requires_auth
def query_data():
    logger.log_request(request)

    request_body = json.loads(request.data, strict=False)
    target_channel = request_body["channel_id"]
    message_id = request_body["message_id"]

    return discord.query_message(target_channel, message_id)

@app.route('/messages/', methods=['PUT'])
@auth.requires_auth
def edit_data():
    logger.log_request(request)
    
    request_body = json.loads(request.data, strict=False)
    target_channel = request_body["channel_id"]
    message_id = request_body["message_id"]
    message_content = request_body["content"]

    discord.edit_message(target_channel, message_id, message_content)
    return {"status": 200}