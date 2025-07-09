from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=100)  
    phone = models.CharField(max_length=15, unique=True)
    is_admin = models.BooleanField(default=False) 

    REQUIRED_FIELDS = ['email', 'phone', 'name']

    def __str__(self):
        return self.email