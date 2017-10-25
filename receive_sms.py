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

    main_counter = session.get('main_counter', 0)
    # sub_counter = session.get('sub_counter', 0)
    # is_sub_question = session.get('sub_question', False)

    question_list = [
            "Have you generated any new ideas?",
            # "Type in the name of the idea and the seed stage",
            "Have you killed any ideas?",
            # "Type in the name of the idea",
            # "Type in the reason for killing the idea",
            "Any ideas on hold now?",
            # "What ideas is on hold?",
            "Any name changes this week?",
            # "From what old name to what new name?",
            "Any ideas advance stages or go backwards?"
            # "Which idea? And from what stage to what stage?"
            ]

    body = request.values.get('Body').lower()
    if 'reset' in body:
        main_counter = 0
    current_question = question_list[main_counter]

    resp = MessagingResponse()

    if body == 'y' or 'yes' in body:
        resp.message("You responded with yes, thanks!\n"
                "(You may respond with N to move on to the next question)")
    elif body == 'n' or 'no' in body:
        main_counter += 1
        resp.message(question_list[main_counter])

    session['main_counter'] = main_counter

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
