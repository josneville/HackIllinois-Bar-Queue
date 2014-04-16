from flask import Flask, render_template, request
from twilio.rest import TwilioRestClient
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/sendText', methods = ['GET', 'POST'])
def send_text():
	if 'phoneNumber' in request.form and 'name' in request.form and 'drink' in request.form:
		account_sid = "AC52f7183ca06b39cd390991416f658abe"
		auth_token  = "8e6423085a1e2a80fc2dbb19edacd49d"
		client = TwilioRestClient(account_sid, auth_token)
		name = str(request.form['name'])
		drink = str(request.form['drink'])
		bodyMessage = "Hey, " + name + "\n" + "Your " + drink + " is ready!"
		phoneNumber = "+1" + str(request.form['phoneNumber'])
		message = client.messages.create(body=bodyMessage, to=phoneNumber, from_="+17542278431")
		return "SUCCESS", 200
	else:
		return "Fail", 300
	
if __name__ == '__main__':
    app.run()
 
