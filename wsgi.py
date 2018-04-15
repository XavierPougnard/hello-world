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
    response = Response("{'status':'VALID'}", status=200)
    response.headers.add('Content-Type', 'application/json')
    return response
	    
@application.route("/payments/pay", methods=['POST'])
def payment_process():
    response = Response("{'status':'SUCCESS'}", status=200)
    response.headers.add('Content-Type', 'application/json')
    return response

if __name__ == "__main__":
    application.run()
