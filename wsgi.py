import json
import stripe
from flask import Flask
from flask import request
application = Flask(__name__)
stripe.api_key = "sk_test_GFPwTzowsn7YzgX4wnPBRfAt"

@application.route("/", methods=['GET'])
def homepage():
    return """
	<!DOCTYPE html>
	<html>
	  <head>
	    <title>Very Easy Parking</title>
	    <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
		<script src="JSlibrary.js" type="text/javascript"></script>
	  </head>
	  <body>
	    <p>
			<img src= 'very easy parking.png'>
		</p>
		<form action="payment/stripe_token" method="POST">
		  <script
		    src="https://checkout.stripe.com/checkout.js" class="stripe-button"
		    data-key="pk_test_aw172A4CceQhwDIc55FJiF1J"
		    data-amount="999"
		    data-name="Xavier Pougnard"
		    data-description="Example charge"
		    data-image="https://stripe.com/img/documentation/checkout/marketplace.png"
		    data-locale="auto"
		    data-currency="eur">
		  </script>
	       </form>
	  </body>
	</html>
    """    

@application.route("/", methods=['POST'])
def get_token0():
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON received'

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

@application.route('/payment/stripe_token', methods=['POST'])
def get_token():
    print (request.is_json)
    content = request.get_json()
    token = content.id
    print (content)
    print (token)
    return token

@application.route('/payment/charge', methods=['GET'])
def process_charge():
    stripe.Charge.create(
	    amount = 1,
		currency = "eur",
		source = "tok_KPte7942xySKBKyrBu11yEpf",
		metadata = {'order_id' : '6735'}
	)
    return "essai ..."	
	
if __name__ == "__main__":
    application.run()
