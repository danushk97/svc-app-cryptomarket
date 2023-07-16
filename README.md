# svc-app-cryptomarket

svc-app-cryptomarket is a microservice that provides simple REST API to retrieve
summary of the cryptocurrency markets. As of now this microservice heavily
relies on Bittrex API in order to fetch summary data.The summary includes
essential information such as symbol, high, low, volume, quote_volume, 
percent_change, updated_at.

# API documentation

For the detailed API documentation and available endpoints, please refer
to the [API DOC](http://127.0.0.1:5000/v3/ui/)

# Installation and setup

Follow this steps to set up and run the service.

## Requirements

This project requires [Python 3.10](https://www.python.org/downloads/release/python-3100/) 
or higher and the [PIP](https://pip.pypa.io/en/stable/) package manager.

## Clone the repository

```console
$ git clone https://github.com/danushk97/svc-app-cryptocurrency
$ cd svc-app-cryptomarket
```

## Create virtualenv

```console
$ python -m venv venv
$ source venv/bin/activate
```

## Install the requirements

```console
$ pip install -r requirements.txt
```

## Run tests

```console
$ pytest
```

## Set environment variables

Ensure that the below environment variables are updated in the file
{FLASK_ENV}.env

```console
$ export BITTREX_API_KEY=<bittrex_api_key>
$ export BITTREX_SECRET_KEY=<bittrex_secret_key>
$ export BITTREX_SERVICE_BASE_URL=https://api.bittrex.com
$ export ALL_MARKETS_SUMMARY_ENDPOINT=/v3/markets/summaries
$ export MARKET_SUMMARY_ENDPOINT=/v3/markets/{market}/summary
$ export LOGGING_LEVEL=DEBUG
$ export ENV=<env>
```

## Run flask app

```console
$ export FLASK_APP=src.app:create_app
$ flask run -p <port>
```