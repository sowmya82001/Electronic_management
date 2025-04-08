from django.contrib import admin
from .models import Product, Supplier, Customer, Sale

admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Sale)