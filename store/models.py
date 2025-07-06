from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone=models.CharField(max_length=15)
    name=models.CharField(max_length=15)

class Address(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    street=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    pin_code=models.CharField(max_length=10)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField()
    image=models.ImageField(upload_to='product_images/')
    stock_quantity=models.PositiveBigIntegerField(default=0)

class CartItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

class Order(models.Model):
    STATUS_CHOICES=(('Pending','Pending'),('Delivered','Delivered'))
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.ForeignKey(Address,on_delete=models.SET_NULL,null=True)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='Pending')
    created_at=models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
