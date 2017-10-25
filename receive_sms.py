# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse

# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def survey():
    """Conduct a short survey via SMS messages."""
    callers = {
        "+14158675310": "Boots",
        "+14158675311": "Virgil",
    }

    counter = session.get('counter', 0)

    question_list = [
            "Have you generated any new ideas?",
            "Have you killed any ideas?",
            # "Type in the name of the idea",
            # "Type in the reason for killing the idea",
            # "Any ideas on hold now?",
            # "What ideas is on hold?",
            # "Any name changes this week?",
            # "From what old name to what new name?",
            # "Any ideas advance stages or go backwards?",
            # "Which idea? And from what stage to what stage?"
            ]

    sub_questions = [
            ["Type in the name of the idea and the seed stage"],
            ["Type in the name of the idea", "Type in the reason for killing the idea"],
            ]

    from_number = request.values.get('From', None)
    current_question = question_list[counter]
    body = request.values.get('Body').lower()

    resp = MessagingResponse()
    current_question = question_list[counter]
    resp.message(current_question)

    if body == 'y' or 'yes' in body:
        resp.message(sub_questions[0][0])
    elif body == 'n' or 'no' in body:
        counter += 1
        resp.message(question_list[counter])
    elif 'reset' in body:
        counter = 0

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
