from app import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages, request, jsonify

import os
import dialogflow
import requests
import json
import pusher

def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    if text:
        text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        return response.query_result.fulfillment_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dialogflow/webhook', methods=['POST'])
def dialogflow_webhook():
    data = request.get_json(silent=True)
    reply = {
            "fulfillmentText": "lol",
    }
    if data['queryResult']['queryText'] == 'yes':
        reply = {
            "fulfillmentText": "Ok. Tickets booked successfully.",
        }

    elif data['queryResult']['queryText'] == 'no':
        reply = {
            "fulfillmentText": "Ok. Booking cancelled.",
        }
    else:
        reply = {
            "fulfillmentText": "sí se pudo",
        }
    return jsonify(reply);


@app.route('/send_message', methods=['POST'])
def send_message():
    # return jsonify("hello");
    message = request.form['message']
    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
    fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
    response_text = { "message":  fulfillment_text }
    return jsonify(response_text)