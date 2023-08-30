#!/usr/bin/python3
"""defining a schema"""
from mongoengine import *
from models.basemodel import BaseModel


class Recipes(BaseModel, Document):
    """Recipe Collection"""
    title = StringField(max_length=1024)
    user_id = StringField(max_length=60, required=True)
