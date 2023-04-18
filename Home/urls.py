#Home is an app

from django.contrib import admin
from django.urls import path
from Home import views

# this process called as urls Dispatcher

urlpatterns = [
   path('',views.index,name='home'),
   path('product',views.product,name='product'),
   path('services',views.services,name='services'),
   path('contact',views.contact,name='contact'),
   path('cart',views.cart,name='cart'),
   
   
   
    
]