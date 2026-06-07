from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField()

    def __str__(self):
        return f'Category: {self.name}'
    

class Brand(models.Model):
    name = models.CharField(max_length=64)
    descriptions = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='products/', default="")
    name = models.CharField(max_length=128)
    barcode = models.CharField(unique=True)
    price = models.FloatField()
    Category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    Brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.price}$'


