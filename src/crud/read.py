from flask import Flask, request
import requests
from __main__ import app

@app.route("/read")
def read():
    return "test"