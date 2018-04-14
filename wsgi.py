import json
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "eh oh"


@application.route("/request_status")
def answer():
    return ("request status")
	    
@application.route("/completion")
def answer2():
    return "completion"


if __name__ == "__main__":
    application.run()
