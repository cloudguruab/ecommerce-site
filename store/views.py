from django.shortcuts import render
from django.http import request
from .models import *

# Create your views here.

def store(request):
    """[here we create a products configuration
    between products in db to store front]"""
    
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)

def about(request):
    context = {}
    return render(request, 'store/about.html', context)

def login(request):
    context = {}
    return render(request, 'store/login.html', context)

def cart(request):
    """[at cart we want to auth the end user
    if they are auth take the order and created item 
    and proceed to validate cx alogn with completion of the
    order.]"""
    pass
        
    # context item bridges data from model to template        
    # context = {'items': items, 'order': order}
    # return render(request, 'store/cart.html', context)

def checkout(request):
    pass
        
    # context item bridges data from model to template        
    # context = {'items': items, 'order': order}
    # return render(request, 'store/checkout.html', context)
    