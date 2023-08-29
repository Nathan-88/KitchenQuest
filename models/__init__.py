#!/usr/bin/python3
"""Initializes the package"""
from mongoengine import connect

connect(db="kitchenquest", host="localhost", port=27017)

