#!/usr/bin/python3
"""Initializes the package"""
from mongoengine import connect
from dotenv import load_dotenv
from os import getenv

load_dotenv()
try:
    connect(host=getenv('MONGO_CONNECTION_URI', '127.0.0.1'), db='kitchenquest')
    print('connecting')
except Exception:
    print('ERROR')
    print(Exception.with_traceback()) 

