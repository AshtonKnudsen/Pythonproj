from __future__ import unicode_literals
from django.db import models 
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Userman(models.Manager):
    def validator(self, postData):
        errors ={}
        if len(postData["first_name"]) < 3:
            errors["firstname"] = "First Name must be more than 3 characters"
        if len(postData["last_name"])< 3:
            errors["lastname"] = "Last Name must be more than 3 characters"
        if not EMAIL_REGEX.match(postData["email_reg"]):
            errors["email"] = "Email is not a valid email"
        if postData["email_reg"] and User.objects.filter(email=postData["email_reg"]).exists():
            errors["special"] = "Email already in use"
        if postData["password_reg"] != postData["confirm"]:
            errors["password"] = "Passwords did not match"
        return errors
    def login(self, postData):
        errors ={}
        try:
            existing = User.objects.get(email = postData["email_login"])
            if bcrypt.checkpw(postData['password_login'].encode(), existing.password.encode()):
                return True
            else:
                errors["pword"] = "Invalid Email and Password Combination"
                return errors
        except:
            errors["login"] = "Invalid Email and Password Combination"
            return errors
    def update_validator(self, postData):
        errors ={}
        if len(postData["first_name"]) < 3:
            errors["firstname"] = "First Name must be more than 3 characters"
        if len(postData["last_name"])< 3:
            errors["lastname"] = "Last Name must be more than 3 characters"
        if not EMAIL_REGEX.match(postData["email_update"]):
            errors["email"] = "Email is not a valid email"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = Userman()

# Create your models here.
