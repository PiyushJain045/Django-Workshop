from django.shortcuts import render
from django.views import View
from .models import Product 
# Create your views here.

class Home(View):
    def get(self, request):
        print("INSIDE GET HOME")

        products = Product.objects.all() 

        print(products[0].price)

        context = {
            'products': products 
        }


        return render(request, "home.html", context)

    def post(self, request):
        pass