Module 3: Cart

1. Views.py

class Cart(View):
    def get(self, request):
        print("INSDIE GET CART")
        return render(request, "cart.html")
    
    def post(self, request):
        print("INSIDE POST CART")
        return render(request, "cart.html")

2. urls.py

path("Your-Cart",views.Cart.as_view(), name="cart")

3. home.html
<li><a href="{% url 'home' %}" class="active">Home</a></li>
<li><a href="{% url 'cart' %}">Cart</a></li>

4. cart.html
{% load static %}

<link rel="stylesheet" href="{% static 'cart.css' %}">

<img src="{% static 'aperture.svg' %}" alt="E-Commerce Logo">

<li><a href="{% url 'home' %}">Home</a></li>

5. Remove Cart item


6. Create a model for cart itme
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

7. Register in admin.py

from django.contrib import admin
from .models import Product, CartItem 

# Register your models here.
admin.site.register(Product)
admin.site.register(CartItem)

8. Apply migrations

9. Now lets add functionality to add item in our cart

home.html
                
{% for product in products %}
 <form method="POST" action="{% url 'cart' %}">
    {% csrf_token %}
         <input type="hidden" name="product_id" value="{{ product.id }}">
                     
           <div class="product-card">
                        <div class="product-image">
                            <img src="{{ product.image.url }}" alt="{{ product.name }}">
                        </div>
                        <div class="product-details">
                            <h3 class="product-title">{{ product.name }}</h3>
                            <p class="product-price">{{ product.price }}</p>
                            <p class="product-description">{{ product.description }}</p>
             <button type="submit" class="add-to-cart-btn">Add to Cart</button>
                        </div>
                    </div>
</form>
{% endfor %}

10. views.py 'Cart'

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

11. cart.html
<!-- Cart Item 1 -->
 {% for item in cart_items %}
                        <tr class="cart-item">
                            <td class="product-info">
                                <img src="{{ item.product.image.url }}" alt="{{ item.product.name }}">
                                <div>
                                    <h3>{{ item.product.name }}</h3>
                                    <p>{{ item.product.description|truncatewords:5 }}</p>
                                </div>
                            </td>
                            <td class="price">₹{{ item.product.price }}</td>
                            <td class="quantity">
                                <button class="quantity-btn decrease">-</button>
                                <input type="number" value="{{ item.quantity }}" min="1" max="10">
                                <button class="quantity-btn increase">+</button>
                            </td>
                            <td class="total">₹₹{{ item.total_price }}</td>
                            <td class="actions">
                                <button class="remove-btn">Remove</button>
                            </td>
                        </tr>
                        {% empty %}
                        <tr>
                            <td colspan="5" style="text-align: center;">Your cart is empty 🛒</td>
                        </tr>
                        {% endfor %}


