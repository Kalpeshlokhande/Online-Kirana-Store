from django.db import models
from django.contrib.auth.models import User
from app.products.models import Product

ORDER_STATUS = (
    ('Pending', 'Pending'),
    ('Delivered', 'Delivered'),
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)