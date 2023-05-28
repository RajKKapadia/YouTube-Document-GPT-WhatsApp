from flask import Flask, request

from document_gpt.helper.conversation import create_conversation
from document_gpt.helper.twilio_api import send_message

qa = create_conversation()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'OK', 200

@app.route('/twilio', methods=['POST'])
def twilio():
    print(request.form.to_dict())
    query = request.form['Body']
    sender_id = request.form['From']
    # TODO
    # get the user
    # if not create
    # create chat_history from the previous conversations
    res = qa(
        {
        'question': query,
        'chat_history': {}
        }
    )
    
    send_message(sender_id, res['answer'])

    return 'OK', 200
