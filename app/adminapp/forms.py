from django import forms
from django.contrib.auth.forms import AuthenticationForm
from app.products.models import Product

class AdminLoginForm(AuthenticationForm):
    username=forms.CharField(label="Username",max_length=150)
    password=forms.CharField(label="Password",widget=forms.PasswordInput)

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields =['name','catrgoey','price','description','image','stock_quantity']