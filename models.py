from django.db import models

# Create your models here.
class Products(models.Model):
    pname=models.CharField(max_length=100)
    price=models.FloatField()
    stock=models.IntegerField()
    pimage=models.CharField(max_length=2500)


