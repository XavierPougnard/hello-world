import json

# issue de request.json
#serial_token = {'transactionId': '85399', 'paymentToken': '{"signatureData":{"merchantId":"03436642101965340153","tokenizationData":{"tokenizationType":"PAYMENT_GATEWAY","parameters":{"gateway":"stripe","stripe:publishableKey":"pk_live_4qnx5Cq8bA6FWxGD52Tg6YYK","stripe:version":"5.1.0"}},"primaryLineItems":[{"label":"Parking ticket","subtext":"1 hour","currencyCode":"EUR","value":"0.10"}],"secondaryLineItems":[{"label":"Tax","currencyCode":"EUR","value":"0.00"}],"total":{"label":"Total","currencyCode":"EUR","value":"0.11"}},"requestSignature":"dummy_signature","responseJson":"{\\\\"cardInfo\\\\":{\\\\"cardNetwork\\\\":\\\\"VISA\\\\",\\\\"cardDetails\\\\":\\\\"6349\\\\",\\\\"cardImageUri\\\\":\\\\"https:\\\\\\\\/\\\\\\\\/lh6.ggpht.com\\\\\\\\/NvYf_33MleY1waJfW6O98wb3KU6XeinwiahmvUIyu46LcWeQdTMGm7WYe81uZYWLUbkjvz0E\\\\",\\\\"billingAddress\\\\":{\\\\"countryCode\\\\":\\\\"FR\\\\",\\\\"postalCode\\\\":\\\\"22300\\\\",\\\\"name\\\\":\\\\"Xavier Pougnard\\\\"},\\\\"cardDescription\\\\":\\\\"Visa\\u2006\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\\u20066349\\\\",\\\\"cardClass\\\\":\\\\"CREDIT\\\\"},\\\\"paymentMethodToken\\\\":{\\\\"tokenizationType\\\\":\\\\"PAYMENT_GATEWAY\\\\",\\\\"token\\\\":\\\\"{\\\\\\\\n  \\\\\\\\\\\\"id\\\\\\\\\\\\": \\\\\\\\\\\\"tok_1CccBcIqolb0nto6HH1fz45E\\\\\\\\\\\\",\\\\\\\\n  \\\\\\\\\\\\"object\\\\\\\\\\\\": \\\\\\\\\\\\"token\\\\\\\\\\\\",\\\\\\\\n  \\\\\\\\\\\\"card\\\\\\\\\\\\": {\\\\\\\\n    \\\\\\\\\\\\"id\\\\\\\\\\\\": \\\\\\\\\\\\"card_1CccBcIqolb0nto6c5gsrUIM\\\\\\\\\\\\",\\\\\\\\n    \\\\\\\\\\\\"object\\\\\\\\\\\\": \\\\\\\\\\\\"card\\\\\\\\\\\\",\\\\\\\\n    \\\\\\\\\\\\"address_city\\\\\\\\\\\\": null,\\\\\\\\n    \\\\\\\\\\\\"address_country\\\\\\\\\\\\": null,\\\\\\\\n    \\\\\\\\\\\\"address_line1\\\\\\\\\\\\": null,\\\\\\\\n    \\\\\\\\\\\\"address_line1_check\\\\\\\\\\\\": null,\\\\\\\\n    \\\\\\\\\\\\"address_line2\\\\\\\\\\\\": null,\\\\\\\\n    \\\\\\\\\\\\"address_state\\\\\\\\\\\\": null,\\\\\\\\n \\\\\\\\\\\\"address_zip\\\\\\\\\\\\": null,\\\\\\\\n \\\\\\\\\\\\"address_zip_check\\\\\\\\\\\\": null,\\\\\\\\n \\\\\\\\\\\\"brand\\\\\\\\\\\\": \\\\\\\\\\\\"Visa\\\\\\\\\\\\",\\\\\\\\n \\\\\\\\\\\\"country\\\\\\\\\\\\": \\\\\\\\\\\\"FR\\\\\\\\\\\\",\\\\\\\\n \\\\\\\\\\\\"cvc_check\\\\\\\\\\\\": null,\\\\\\\\n \\\\\\\\\\\\"dynamic_last4\\\\\\\\\\\\": \\\\\\\\\\\\"6349\\\\\\\\\\\\",\\\\\\\\n \\\\\\\\\\\\"exp_month\\\\\\\\\\\\": 10,\\\\\\\\n \\\\\\\\\\\\"exp_year\\\\\\\\\\\\": 2020,\\\\\\\\n \\\\\\\\\\\\"funding\\\\\\\\\\\\": \\\\\\\\\\\\"debit\\\\\\\\\\\\",\\\\\\\\n \\\\\\\\\\\\"last4\\\\\\\\\\\\": \\\\\\\\\\\\"6349\\\\\\\\\\\\",\\\\\\\\n \\\\\\\\\\\\"metadata\\\\\\\\\\\\": {},\\\\\\\\n \\\\\\\\\\\\"name\\\\\\\\\\\\": null,\\\\\\\\n \\\\\\\\\\\\"tokenization_method\\\\\\\\\\\\": \\\\\\\\\\\\"android_pay\\\\\\\\\\\\"\\\\\\\\n },\\\\\\\\n \\\\\\\\\\\\"client_ip\\\\\\\\\\\\": \\\\\\\\\\\\"74.125.177.34\\\\\\\\\\\\",\\\\\\\\n \\\\\\\\\\\\"created\\\\\\\\\\\\": 1528908668,\\\\\\\\n \\\\\\\\\\\\"livemode\\\\\\\\\\\\": true,\\\\\\\\n \\\\\\\\\\\\"type\\\\\\\\\\\\": \\\\\\\\\\\\"card\\\\\\\\\\\\",\\\\\\\\n \\\\\\\\\\\\"used\\\\\\\\\\\\": false\\\\\\\\n}\\\\\\\\n\\\\"}}"}'}


def getToken(serialToken):
    serialToken2=json.dumps(serialToken)
    token = ''
    for i in range (1,len(serialToken2)-4):
        keyX = serialToken2[i]+serialToken2[i+1]+serialToken2[i+2]+serialToken2[i+3]
        if keyX=='tok_':
	        j=0
	        while serialToken2[i+j] != '\\' :
		        token = token + serialToken2[i+j]
		        j=j+1
    return(token)

			
# stripeToken = getToken(serial_token)

