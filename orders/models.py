from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total(self):
        total = self.quantity * self.product.price
        return total

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=255, blank=True)
    items = models.ManyToManyField(CartItem, through='CartItemInCart')

    def __str__(self):
        return f'Cart of {self.user.username}'

class CartItemInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    cart_item = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total(self):
        return self.cart_item.get_total()

    def __str__(self):
        return f'{self.quantity} of {self.cart_item}'

    def update_total(self):
        return self.cart_item.get_total() - self.cart_item.product.price
