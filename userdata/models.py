from django.db import models

# Create your models here.
class userdata(models.Model):
     name=models.CharField(max_length=50)
     email=models.EmailField(max_length=50,unique=True)
     password=models.CharField(max_length=50)

class compony(models.Model):
     name=models.CharField(max_length=50)
     email=models.EmailField(max_length=50,unique=True)
     password=models.CharField(max_length=50)