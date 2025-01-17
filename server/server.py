#! /usr/bin/env python3.6

import stripe
import json
import os

from flask import Flask, render_template, jsonify, request, send_from_directory
from dotenv import load_dotenv, find_dotenv

# Setup Stripe python client library
load_dotenv(find_dotenv())
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

app = Flask(__name__,
    static_folder='../client', static_url_path="", template_folder='../client')



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


#@app.route('/public-keys')
#def public_keys():
 #   return jsonify({"key": os.getenv("STRIPE_PUBLISHABLE_KEY")})


@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    try:
        # data = json.loads(request.data)
        intent = stripe.PaymentIntent.create(
            amount=1400,
            currency='usd'

        )
        # return intent
        return jsonify({
          'clientSecret': intent["client_secret"]
        })
    except Exception as e:
        return jsonify(error=str(e)), 403


@app.route('/webhook', methods=['POST'])
def webhook_received():
    # You can use webhooks to receive information about asynchronous payment events.
    # For more about our webhook events check out https://stripe.com/docs/webhooks.
    webhook_secret = os.getenv('STRIPE_WEBHOOK_SECRET')
    request_data = json.loads(request.data)

    with open("server/logs.json") as f:
        logs = json.load(f)

    if webhook_secret:
        # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
        signature = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload=request.data, sig_header=signature, secret=webhook_secret)
            data = event['data']

        except Exception as e:
            return e
        # Get the type of webhook event sent - used to check the status of PaymentIntents.
        event_type = event['type']
    else:
        data = request_data['data']
        event_type = request_data['type']
        data_object = data['object']

    print('event ' + event_type)

    if event_type == 'some.event':
        print('Webhook received!')

    if event_type == 'payment_intent.succeeded':
        logs["payment_intent.succeeded"].append({"amount": data['object']['amount'],
                                                 "billing_details": data['object']['charges']['data'][0]['billing_details']} )
        with open('server/logs.json', 'w') as outfile:
            json.dump(logs, outfile)

    return jsonify({'status': 'success'})


if __name__== '__main__':
    app.run(port=4242)

