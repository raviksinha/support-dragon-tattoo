# dragon-tattoo-on-sale
Dummy ecommerce site with python-flask backend and Stripe integration

To run do the following
## Create a virtual environment
python3 -m venv env

## Activate the environmennt
. ./env/bin/activate

### Save Stripe Keys in .env file with the following structure 
#Stripe API keys - see https://stripe.com/docs/development/quickstart#api-keys

STRIPE_PUBLISHABLE_KEY=''
STRIPE_SECRET_KEY= ''

#### Required to run webhook
#### See README on how to use the Stripe CLI to setup
#### Ignore when running `without-webhooks` samples
STRIPE_WEBHOOK_SECRET= ''

Environment setup (web client)
STATIC_DIR=../../client/web

## Install requireme\nts 
pip install -r requirements.txt

## Run the service 
python3 server/server.py
