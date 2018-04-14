#essai1
import json
from flask import Flask # pip install flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "eh oh"


@app.route("/request_status")
def answer():
    content_dic = {"bot id" : "ezy-park", "user": "Xavier"}
    messageX = json.dumps(content_dic, indent=4)
    print(messageX)
    return messageX

	
@app.route("/completion")
def answer2():
    content_dic2 = {"bot id" : "ezy-park2", "user": "Xavier2"}
    messageY = json.dumps(content_dic2, indent=4)
    print(messageY)
    return messageY


if __name__ == "__main__":
    app.run()