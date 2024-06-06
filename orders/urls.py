from django.urls import path
from . import views

app_name = 'orders'  # Define the namespace

urlpatterns = [
    path('add-to-cart/', views.addToCart, name='addToCart'),
    path('view-cart/', views.viewCart, name='viewCart'),
    path('remove-from-cart/<int:item_id>/', views.removeFromCart, name='removeFromCart'),
    #path('', views.store, name='store')''',
]
