from django.db import models
from django.contrib.auth.models import User


class Content(models.Model):
    title = models.CharField(max_length=100)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)

