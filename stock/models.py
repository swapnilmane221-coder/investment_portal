from django.db import models

class transactionhistory(models.Model):
     Date=models.DateField()
     name=models.CharField(max_length=50)
     amount=models.FloatField()
     quantity=models.IntegerField()
     status=models.CharField(max_length=50)
     total_amount=models.FloatField()
# Create your models here.
