#!/usr/bin/python3
from models.users import Users
from models.recipes import Recipes

user1 = Users(username="yello_yagain", password="world")
user1.save()

user_id = str(user1.id)
recipe1 = Recipes(title="An Interesting recipe", user_id=user_id)
recipe1.save()
