from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inventory/', views.inventory_status, name='inventory_status'),
    path('customers/', views.customer_history, name='customer_history'),
    path('suppliers/', views.supplier_performance, name='supplier_performance'),
]