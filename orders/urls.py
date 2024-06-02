from django.urls import path
from . import views

app_name = 'orders'  # Define the namespace

urlpatterns = [
    path('add-to-cart/', views.addToCart, name='addToCart'),
    #path('view-cart/', views.view_cart, name='viewCart'),
    #path('remove-from-cart/', views.remove_from_cart, name='removeFromCart'),
    #path('', views.store, name='store')''',
]
