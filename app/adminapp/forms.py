from django import forms
from app.products.models import Product, Category
from django.contrib.auth.models import User

class AdminRegisterForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields=['username' ,'email' , 'password']

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            confirm = cleaned_data.get('confirm_password')
            if password and confirm and password != confirm:
                raise forms.ValidationError("Passwords do not match")
            return cleaned_data

class AdminLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'stock_quantity', 'description', 'image']