from __future__ import unicode_literals
from django.db import models
from apps.LoginReg.models import User

class Postmanager(models.Manager):
    def post_validator(self,postData):
        errors={}
        if len(postData["author"])< 5:
            errors["author_name"] = "This Author needs some recognition"
        if len(postData["quotes"])< 5:
            errors["quote_data"] = "What they dont talk much? sure."
        return errors

class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts")
    author_name = models.CharField(max_length=45)
    user_name = models.CharField(max_length=45)
    message = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = Postmanager()