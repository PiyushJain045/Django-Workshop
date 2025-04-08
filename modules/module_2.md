Module 2

1. Import and HTML and CSS files in our 'e_commerce' app


2. Project lvl urls.py 
```bash
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('e_commerce.urls')),
]

App-level urls.py
```bash
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
]


//the urls.py file is responsible for URL routing — it maps specific URLs (the paths users type in their browser) to corresponding views
// name="home" :- Lets name the route 'home' which we will use in our templates

3. Views.py

from django.shortcuts import render
from django.views import View
# Create your views here.

class Home(View):
    def get(self, request):
        print("INSIDE GET HOME")
        return render(request, "home.html")

    def post(self, request):
        pass

4. Connect in home.html

{% load static %}
<link rel="stylesheet" href="{% static 'home.css' %}">
<img src="{% static 'aperture.svg' %}" alt="E-Commerce Logo">

Remove product 2,3,4

5. Models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product-images/', null=True, blank=True)

    def __str__(self):
        return self.name

6. Install Pillow //Pillow is a Python Imaging Library that Django uses to handle image files.

6. admin.py
from django.contrib import admin
from .models import Product

# Register your models here.
admin.site.register(Product)


7. Perform migrations 
python manage.py makemigrations //Tells Django to detect changes in your models.py
python manage.py migrate //Applies those migrations

8. Try to access admin panel but superuser is required
python manage.py createsuperuser

9. Add product to a database

10. Serving Uploaded Media Files

In settings.py

MEDIA_URL = "/files/"
MEDIA_ROOT = BASE_DIR 

In Project-Level urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

11. views.py
from .models import Product 

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

12. home.html
DTL product Card

{% for product in products %}
                <div class="product-card">
                    <div class="product-image">
                        <img src="{{ product.image.url }}" alt="{{ product.name }}">
                    </div>
                    <div class="product-details">
                        <h3 class="product-title">{{ product.name }}</h3>
                        <p class="product-price">{{ product.price }}</p>
                        <p class="product-description">{{ product.description }}</p>
                        <button class="add-to-cart-btn">Add to Cart</button>
                    </div>
                </div>
{% endfor %}

13. End Rest of the products in the database
