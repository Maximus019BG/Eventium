from django.db import models

# Create your models here.
class User(models.Model):
    username= models.CharField(max_length=25,blank=False,null=False)
    password= models.CharField(max_length=16,blank=False,null=False)
    age= models.IntegerField(null=False, blank=False,)