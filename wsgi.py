import json
import stripe
from flask import Flask, request, redirect
from flask import render_template, url_for
application = Flask(__name__)

pub_key = "pk_test_aw172A4CceQhwDIc55FJiF1J"
secret_key = "sk_test_GFPwTzowsn7YzgX4wnPBRfAt"

stripe.api_key = secret_key

@application.route("/", methods=['GET'])
def homepage():
    global amountX 
    amountX = int(request.args.get('amount'))
    return render_template('index.html', pub_key=pub_key, amount=amountX)    
    
@application.route('/payment/status', methods=['GET'])
    #Check internal systems to determine if transactionId URL parameter is valid or expired
    #If valid, return 200 OK with valid status in JSON payload: {"status":"VALID"}
    #If expired, return 200 OK with expired status in JSON payload: {"status":"EXPIRED"}
    #content = {'status':'VALID'}
    #return content
def expire_check():
    print('payment_status')
    content = {'status':'VALID'}
    messageX = json.dumps(content, indent=4)
    return messageX


@application.route('/payment/pay', methods=['POST'])
def process_payment():
    print('payment_pay')
    contentPost = request.json
    print(contentPost)
    content = {'status':'SUCCESS'}
    messageY = json.dumps(content, indent=4)
    return messageY

@application.route('/stripe/events', methods=['POST'])
def stripe_event():
    print('Stripe_event')
    contentPost = request.json
    print(contentPost)
    content = {'status':'SUCCESS'}
    messageY = json.dumps(content, indent=4)
    return messageY

@application.route('/payment/charge', methods=['POST'])
def charge():
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer=customer.id,
	amount=amountX,
	currency='eur',
	description='parking'
    )
    return redirect(url_for('thanks'))	

@application.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == "__main__":
    application.run()
