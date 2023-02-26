from flask import Flask
import requests
import resources
import json

CONFIG = dict(json.load(open("config.json")))

app = Flask(__name__)

@app.route('/log/')
def send_log_id():
    return {CONFIG["LOG_CHANNEL_ID"], 200}

@app.route('/user/')
def send_users_id():
    return {CONFIG["USERS_CHANNEL_ID"], 200}

resources.establish_resources()

if __name__ == "__main__":
    app.run()