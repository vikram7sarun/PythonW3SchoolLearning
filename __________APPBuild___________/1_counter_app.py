from flask import Flask, app


@app.route("/")
def home():
    return "Hello World"


app = Flask(__name__)
# app.run(host='0.0.0.0', port=81)