from flask import Flask, request
import json
from tools import discord, logger, auth

from __main__ import app

@app.route('/messages/', methods=['POST'])
@auth.requires_auth
def upload_data():
    logger.log_request(request)
    try:
        request_body = json.loads(request.data, strict=False)
        target_channel = request_body["channel_id"]
        message_content = request_body["content"]

        discord.send_message(target_channel, message_content)
    except:
        return { "status" : "error", "message": "Data upload failed" }, 400
    
    return { "status" : "success", "message": "Data uploaded successfully"}, 200

@app.route('/messages/', methods=['DELETE'])
@auth.requires_auth
def delete_data():
    logger.log_request(request)

    try:
        request_body = json.loads(request.data, strict=False)
        target_channel = request_body["channel_id"]
        message_id = request_body["message_id"]

        discord.delete_message(target_channel, message_id)
    except:
        return { "status" : "error", "message": "Data deletion failed" }, 400

    return { "status" : "success", "message": "Data deleted successfully" }, 200

@app.route('/messages/', methods=['GET'])
@auth.requires_auth
def query_data():
    logger.log_request(request)
    try:
        request_body = json.loads(request.data, strict=False)
        target_channel = request_body["channel_id"]
        message_id = request_body["message_id"]
        message_content = discord.query_message(target_channel, message_id)
    except:
        return { "status" : "error", "message": "Data retrieval failed" }, 400

    return { "status" : "success", "message": "Data retrieved successfully", "content": message_content }, 200

@app.route('/messages/', methods=['PUT'])
@auth.requires_auth
def edit_data():
    logger.log_request(request)
    try:
        request_body = json.loads(request.data, strict=False)
        target_channel = request_body["channel_id"]
        message_id = request_body["message_id"]
        message_content = request_body["content"]
    except:
        return { "status" : "error", "message": "Edit failed" }, 400

    discord.edit_message(target_channel, message_id, message_content)
    return { "status" : "success", "message": "Data edited successfully" }, 200