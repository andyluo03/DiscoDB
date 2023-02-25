from flask import Flask
import requests
import resources

app = Flask(__name__)
resources.establish_resources()

if __name__ == "__main__":
    app.run()