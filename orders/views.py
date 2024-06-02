from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem, CartItemInCart

@login_required
def addToCart(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_price = request.POST.get('item_price')
        product = Product.objects.get(name=item_name, price=item_price)
        
        return render(request, "store.html", {})