from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cover = models.ImageField(upload_to='cover/', null=True)
    benefits = models.TextField(null=True, blank=True)
    variants = models.TextField(null=True, blank=True)
    weight = models.TextField(null=True, blank=True)
    # cover = models.ImageField(upload_to='cover/', null=True)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    content = models.TextField()
    rating = models.IntegerField()
