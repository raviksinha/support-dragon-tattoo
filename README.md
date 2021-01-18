# dragon-tattoo-on-sale
Dummy ecommerce site with python-flask backend and Stripe integration

To run do the following
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
run `stripe listen --forward-to localhost:4242/webhook`
copy Ready! Your webhook signing secret is `<YOUR_STRIPE_WEBHOOK_SECRET>`


## Install requirements 
`pip install -r requirements.txt`

## Run 
`python3 server/server.py`
