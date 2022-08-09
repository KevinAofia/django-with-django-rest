from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)


