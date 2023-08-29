#!/usr/bin/python3
"""defining the base attributes for all schemas"""
from datetime import datetime
from mongoengine import *


class BaseModel:
    """common fields"""
    created_at = DateTimeField(default=datetime.now())
    modified_at = DateTimeField(default=datetime.now())
