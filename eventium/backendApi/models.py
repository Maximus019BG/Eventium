from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=25, blank=False, )
    password = models.CharField(max_length=25, blank=False, )
class Posts(models.Model):
    username = models.CharField(max_length=25, blank=False, )
    description = models.CharField(max_length=25, blank=False, )
    time = models.DateTimeField(auto_now_add=True)