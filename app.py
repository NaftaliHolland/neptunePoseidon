from flask import Flask
import os
import requests
from flask import request
from flask import jsonify

app = Flask(__name__)
print(__name__)
print(type(__name__))


CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]

def exchange_code(code):
    url = "https://github.com/login/oauth/access_token"
    headers = {
            "Accept": "application/json",
            }
    data = {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code
        }
    response = requests.post(url, data=data, headers=headers)

    print(response.json())
    

@app.route("/")
def authenticate_app():

    return f'<a href="https://github.com/login/oauth/authorize?client_id={CLIENT_ID}"> Login with GitHub</a>'

@app.route("/callback", methods=["GET"])
def get_access_token():
    body = request.args
    exchange_code(body["code"])

    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
