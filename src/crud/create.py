from flask import Flask, request
import requests
import json
from __main__ import app

@app.route("/create")
def create():
    body = json.loads(request.data, strict=False)
    channel = body["channel"]
    data = body["data"]

    

    return "Success!"
