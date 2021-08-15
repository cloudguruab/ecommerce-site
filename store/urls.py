from django.urls import path 
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.login, name='login'),
    path('checkout/', views.checkout, name='checkout'),
]