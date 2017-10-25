# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def survey():
    """Conduct a short survey via SMS messages."""
    callers = {
        "+14158675310": "Boots",
        "+14158675311": "Virgil",
    }

    from_number = request.values.get('From', None)
    body = request.values.get('Body').lower()

    resp = MessagingResponse()
    if body == 'y' or 'yes' in body:
        resp.message("Type in the name of the idea and the seed stage")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
