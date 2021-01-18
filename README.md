# support-dragon-tattoo
Dummy ecommerce site with python-flask backend and Stripe integration


## Create a virtual environment
`python3 -m venv env`

## Activate the environmennt
`. ./env/bin/activate`

## Create .env file with the following keys 
```
STRIPE_PUBLISHABLE_KEY=''
STRIPE_SECRET_KEY= ''
STRIPE_WEBHOOK_SECRET= ''
```

##### For `STRIPE_PUBLISHABLE_KEY`, `STRIPE_SECRET_KEY`
see https://stripe.com/docs/development/quickstart#api-keys


##### For `STRIPE_WEBHOOK_SECRET`:
Install STRIPE CLI, see https://stripe.com/docs/stripe-cli


run `stripe listen --forward-to localhost:4242/webhook`


The console should display: Ready! Your webhook signing secret is `<YOUR_STRIPE_WEBHOOK_SECRET>`



## Install requirements 
`pip install -r requirements.txt`

## Run 
`python3 server/server.py`


## Find
Logs for completed orders to be fullfilled can be seen in `server/logs.json`
