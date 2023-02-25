from flask import Flask
import requests
import crud

app = Flask(__name__)
crud.establish_crud()

if __name__ == "__main__":
    app.run()