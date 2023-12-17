from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=24,default='',unique=True)
    password = models.CharField(max_length=30,default='')

class Posts(models.Model):
    name = models.CharField(max_length=50,default='Събитие')
    description = models.CharField(max_length=250, blank=False,)
    time = models.DateTimeField(auto_now_add=True)

