from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages

from .models import Product, Cart, CartItem, CartItemInCart

@login_required
def addToCart(request):
    if request.method == 'POST':
        product_name = request.POST.get('item_name')
        product_price = request.POST.get('item_price')
        product, created = Product.objects.get_or_create(name=product_name, price=product_price)
        
        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(product=product, defaults={'quantity': 1})
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        cart_item_in_cart, created = CartItemInCart.objects.get_or_create(cart=cart, cart_item=cart_item)
        if not created:
            cart_item_in_cart.quantity += 1
            cart_item_in_cart.save()
        
        messages.success(request, f'{product.name} was added to your cart successfully!')
        return render(request, "store.html")

@login_required
def viewCart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItemInCart.objects.filter(cart=cart)
    total_price = sum(item.get_total() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def removeFromCart(request, item_id):
    cart_item_in_cart = get_object_or_404(CartItemInCart, id=item_id)
    cart_item_in_cart.cart.items.remove(cart_item_in_cart.cart_item) 
    cart_item_in_cart.cart_item.delete()  
    cart_item_in_cart.delete()  

    return redirect('orders:viewCart')