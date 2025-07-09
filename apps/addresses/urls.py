from django.urls import path
from apps.addresses.views.address import UpdateAddressView

urlpatterns = [
    path('profile/address', UpdateAddressView.as_view()),
]