import os
from flask import Flask, render_template, request
import africastalking

app = Flask(__name__)

username = "sandbox"
api_key = ""

africastalking.initialize(username, api_key)

@app.route("/", methods=["POST"])
def index():
	if request.method == "POST":
		airtime_amount = request.form[]
		phone_number = request.form[]

		print(airtime_amount)
		print(phone_number)

		response = airtime.send(airtime_amount, [phone_number])

	return render_template('index.html')

if __name__ == "__main__":
    app.run(port=os.environ.get('PORT'))