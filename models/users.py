#!/usr/bin/python3
"""defining the schema for users collection"""
from mongoengine import *
from models.basemodel import BaseModel


class Users(BaseModel, Document):
    """users Collection in KitchenQuest db"""
    username = StringField(max_length=120, required=True, unique=True)
    password = StringField(max_length=120, required=True)
    saved_recipes = ListField(StringField(unique=True), default=[])

