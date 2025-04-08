from django.shortcuts import render
from .models import Product, Sale, Customer, Supplier
from django.db.models import Sum


def home(request):
    return render(request, 'shop/home.html')

def inventory_status(request):
    products = Product.objects.all()
    low_stock = products.filter(stock__lt=10)
    
    context = {
        'products': products,
        'low_stock_ids': [product.id for product in low_stock],  # for conditional rendering
    }
    return render(request, 'shop/inventory.html', context)
def customer_history(request):
    customers = Customer.objects.all()
    return render(request, 'shop/customers.html', {'customers': customers})

def supplier_performance(request):
    suppliers = Supplier.objects.all()
    return render(request, 'shop/suppliers.html', {'suppliers': suppliers})