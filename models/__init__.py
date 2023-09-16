#!/usr/bin/python3
"""Initializes the package"""
from mongoengine import connect
from dotenv import load_dotenv
from os import getenv

load_dotenv()

host = getenv('MONGO_CONNECTION_URI', '127.0.0.1')
try:
    print('connecting')
    db = connect(db='kitchenquest', host=host, port=27017)
    print(f'db: {db}')
except Exception as error:
    print('ERROR')
    print(f'{type(error).__name__}: {error}')

