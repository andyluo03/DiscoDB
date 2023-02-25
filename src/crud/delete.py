from flask import Flask, request
import requests
from __main__ import app

@app.route("/delete")
def delete():
    return "test"