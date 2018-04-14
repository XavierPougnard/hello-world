import json
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "eh oh"


@application.route("/request_status")
def answer():
    content_dic = {"bot id" : "ezy-park", "user": "Xavier"}
    messageX = json.dumps(content_dic, indent=4)
    return messageX
	    
@application.route("/completion")
def answer2():
    content_dic2 = {"bot id" : "ezy-park2", "user": "Xavier2"}
    messageY = json.dumps(content_dic2, indent=4)
    return messageY

if __name__ == "__main__":
    application.run()
