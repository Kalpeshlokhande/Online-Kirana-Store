from django.db import models
from apps.users.models import User

class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}"