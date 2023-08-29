#!/usr/bin/python3
"""defining a schema"""
from mongoengine import *
from models.basemodel import BaseModel


class Favourites(BaseModel, Document):
    """Favourites Collection"""
    user_id = StringField(max_length=60, required=True)
    recipe_id = StringField(max_length=60, required=True)
