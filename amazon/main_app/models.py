from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.CharField(max_length=100)

class Review(models.Model):
  review = models.CharField(max_length=100)
  rating = models.CharField(max_length=100)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)

