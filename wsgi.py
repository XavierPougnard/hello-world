import json
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "eh oh"


@application.route('/payment/status', methods=['GET'])
    #Check internal systems to determine if transactionId URL parameter is valid or expired
    #If valid, return 200 OK with valid status in JSON payload: {"status":"VALID"}
    #If expired, return 200 OK with expired status in JSON payload: {"status":"EXPIRED"}
    #content = {'status':'VALID'}
    #return content
def expire_check():
    content = {'status':'VALID'}
    messageX = json.dumps(content, indent=4)
    return messageX


@application.route('/payment/pay', methods=['POST'])
def process_payment():
    content = {'status':'SUCCESS'}
    messageY = json.dumps(content, indent=4)
    return messageY

if __name__ == "__main__":
    application.run()
