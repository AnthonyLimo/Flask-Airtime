import os
from flask import Flask, render_template, request
import africastalking

app = Flask(__name__)

username = "sandbox"
api_key = "ENTER_API_KEY_HERE"

africastalking.initialize(username, api_key)

airtime = africastalking.Airtime

@app.route("/", methods=["POST","GET"])
def index():
	if request.method == "POST":
		airtime_amount = request.form["airtimeAmount"]
		phone_number = request.form["phoneNumber"]
		country_code = "KES"

		recipients = [{
			"phoneNumber": phone_number,
			"amount": airtime_amount,
			"currency_code": "KES"  
		}]
		

		response = airtime.send(recipients=recipients)

		print(response)



	return render_template('index.html')

if __name__ == "__main__":
    app.run(port = os.environ.get('PORT'))