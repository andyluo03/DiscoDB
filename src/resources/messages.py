from flask import Flask, request
import json
from tools import discord_crud, json_tools, logger

from __main__ import app

@app.route('/messages/', methods=['POST'])
def upload_data():
    logger.log_request(request)

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

    request_body = json.loads(request.data, strict=False)
    target_channel = request_body["channel_id"]
    message_id = request_body["message_id"]

    discord_crud.delete_message(target_channel, message_id)

    return {"status": 200}

@app.route('/messages/', methods=['GET'])
def query_data():
    logger.log_request(request)

    request_body = json.loads(request.data, strict=False)
    target_channel = request_body["channel_id"]
    message_id = request_body["message_id"]

    return discord_crud.query_message(target_channel, message_id)

@app.route('/messages/', methods=['PUT'])
def edit_data():
    logger.log_request(request)
    
    request_body = json.loads(request.data, strict=False)
    target_channel = request_body["channel_id"]
    message_id = request_body["message_id"]
    message_content = request_body["content"]

    if not json_tools.verify_json(message_content):
        logger.log_failure(400)
        return {"status": 400, "error": "JSON is not formatted correctly"}

    discord_crud.edit_message(target_channel, message_id, message_content)
    return {"status": 200}