from flask import Flask
import resources
from config import USERS_CHANNEL_ID, LOG_CHANNEL_ID

app = Flask(__name__)

@app.route('/log/')
def send_log_id():
    return {"channel_id": LOG_CHANNEL_ID}, 200

@app.route('/user/')
def send_users_id():
    return {"channel_id": USERS_CHANNEL_ID}, 200

resources.establish_resources()

if __name__ == "__main__":
    app.run()