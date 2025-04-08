from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home.as_view(), name="home"),
    path("Your-Cart",views.Cart.as_view(), name="cart")
]