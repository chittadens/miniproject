import email
from django.db import models


class Registration(models.Model):
    username=models.TextField(max_length=10)
    password=models.TextField(max_length=8)
    email=models.EmailField(max_length=25)
    age=models.IntegerField()
   
    class Meta:
        db_table='registration'

class Product(models.Model):
    productname=models.TextField()
    price=models.IntegerField()
    description=models.TextField()
    images=models.CharField(max_length=100)

    
    class Meta:
        db_table='products'


