from django.urls import path
from apps.products.views.category import CategoryListView
from apps.products.views.product import ProductListView

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('products/', ProductListView.as_view()),
]