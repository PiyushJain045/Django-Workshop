from django.shortcuts import render, redirect
from django.views import View
from .models import Product, CartItem
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


class Cart(View):
    def get(self, request):
        print("INSIDE GET CART")
        cart_items = CartItem.objects.all()
        for item in cart_items:
            item.total_price = item.product.price * item.quantity
        return render(request, "cart.html", {"cart_items": cart_items})
    
    def post(self, request):
        print("INSIDE POST CART")
        product_id = request.POST.get("product_id")

        try:
            product = Product.objects.get(id=product_id)
            # Check if product already in cart, increment quantity
            cart_item, created = CartItem.objects.get_or_create(product=product)
            if not created:
                cart_item.quantity += 1
                cart_item.save()
        except Product.DoesNotExist:
            pass  # Optionally handle error

        return redirect("cart")