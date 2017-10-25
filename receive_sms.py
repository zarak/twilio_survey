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
    is_main_question = session.get('is_main_question', True)

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

    sub_question_list = [
            "Type in the name of the idea and the seed stage",
            "Type in the name of the idea",
            # "Type in the reason for killing the idea",
            "What ideas is on hold?",
            "From what old name to what new name?",
            "Which idea? And from what stage to what stage?"
            ]

    questions = list(zip(question_list, sub_question_list))

    body = request.values.get('Body').lower()
    resp = MessagingResponse()

    num_questions = len(question_list)
    if 'reset' in body:
        main_counter = 0
        is_main_question = True

    if main_counter >= num_questions:
        main_counter = 0
        is_main_question = True
        resp.message("That's the end of the survey. Thanks for your time!")
    else:

        if is_main_question == True:
            if body == 'y' or 'yes' in body:
                is_main_question = False
            else:
                main_counter += 1
            
            resp.message(questions[main_counter][not is_main_question])
        else:
            is_main_question = True
            resp.message(questions[main_counter][not is_main_question])
            main_counter += 1

    session['main_counter'] = main_counter
    session['is_main_question'] = is_main_question
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
