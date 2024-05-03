from django.db import models

# Create your models here.

# ini model atau fields product ini digunakan untuk menampilkan list product, product detail dan untuk menambahkan product
# yg wajib diisi hanya name dan description
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cover = models.ImageField(upload_to='cover/', null=True, blank=True)
    benefits = models.TextField(null=True, blank=True)
    variants = models.TextField(null=True, blank=True)
    weight = models.TextField(null=True, blank=True)
    # cover = models.ImageField(upload_to='cover/', null=True)

# model atau fields review ini digunakan user untuk menambahkan review, ada field author karena kami tidak memakai auth/tidak login dulu, jadi untuk penandaan nya kami menggunakan author
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    content = models.TextField()
    rating = models.IntegerField()
