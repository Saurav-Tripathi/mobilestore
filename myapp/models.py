from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    email =  models.EmailField()
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    dis_price = models.IntegerField()
    des = models.TextField()
    img = models.ImageField(upload_to="images")
    def __str__(self):
        return self.name

class Cart(models.Model):
   user=models.ForeignKey(Registration,on_delete=models.CASCADE)
   prod = models.ForeignKey(Product,on_delete=models.CASCADE)
   quantity = models.PositiveIntegerField(default=1)
   subtotal = models.IntegerField()