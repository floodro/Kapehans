from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Product, Cart, CartItem, CartItemInCart

@login_required
def addToCart(request):
    if request.method == 'POST':
        product_name = request.POST.get('item_name')
        product_price = request.POST.get('item_price')
        product, created = Product.objects.get_or_create(name=product_name, price=product_price)
        
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        cart_item, created = CartItem.objects.get_or_create(product=product)
        cart_item.quantity += 1
        cart_item.save()
        
        CartItemInCart.objects.create(cart=cart, cart_item=cart_item, quantity=cart_item.quantity)
        
        return JsonResponse({'message': 'Item added to cart'})
    
def viewCart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItemInCart.objects.filter(cart=cart)
    total_price = sum(item.get_total() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})