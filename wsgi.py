import json
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "eh oh"


@application.route("/payment/status", methods=['GET'])
def expire_check():
    #Check internal systems to determine if transactionId URL parameter is valid or expired
    #If valid, return 200 OK with valid status in JSON payload: {"status":"VALID"}
    #If expired, return 200 OK with expired status in JSON payload: {"status":"EXPIRED"}
    content = {'status':'VALID'}
    return content
	    
@application.route("/payment/pay", methods=['POST'])
def payment_process():
    content = {'status':'SUCCESS'}
    return content

if __name__ == "__main__":
    application.run()
