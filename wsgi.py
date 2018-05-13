import json
import stripe
from flask import Flask, request, redirect
from flask import render_template, url_for
application = Flask(__name__)

pub_key = "pk_test_aw172A4CceQhwDIc55FJiF1J"
secret_key = "sk_test_GFPwTzowsn7YzgX4wnPBRfAt"
amount = 999

stripe.api_key = secret_key

@application.route("/", methods=['GET'])
def homepage():
    #return render_template('index.html', pub_key=pub_key, amount=amount)    
    return '''
	<!DOCTYPE html>
		<html>
		  <head>
		    <title>Ezy-Park</title>
		    <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
			<script src="JSlibrary.js" type="text/javascript"></script>
		  </head>
		  <body>
		    Welcome to Ezy-Park !!!
			<p>
				<img src= 'very easy parking.png'>
			</p>
			<form action="payment/charge" method="POST">
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
	'''

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

@application.route('/payment/charge', methods=['POST'])
def charge():
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer=customer.id,
	amount=amount,
	currency='eur',
	description='parking'
    )
    return redirect(url_for('thanks'))	

@application.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == "__main__":
    application.run()
