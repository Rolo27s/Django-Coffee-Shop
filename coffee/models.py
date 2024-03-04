from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)

class CartList(models.Model):
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    quantity = models.IntegerField()