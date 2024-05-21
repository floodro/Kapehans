let cartItems = [];

function addToCart(coffeeName) {
    let sizeElement = document.getElementById(coffeeName.toLowerCase() + '-size');
    let size = sizeElement.options[sizeElement.selectedIndex].text.split(' - ')[0];
    let price = parseFloat(sizeElement.value);

    let toppings = [];
    let pearlsCheckbox = document.getElementById(coffeeName.toLowerCase() + '-pearls');
    if (pearlsCheckbox && pearlsCheckbox.checked) {
        toppings.push({ name: 'Pearls', price: 10.00 });
        price += 10.00; 
    }
    let crystalsCheckbox = document.getElementById(coffeeName.toLowerCase() + '-crystals');
    if (crystalsCheckbox && crystalsCheckbox.checked) {
        toppings.push({ name: 'Crystals', price: 10.00 });
        price += 10.00;
    }

    
    let lemonCheckbox = document.getElementById(coffeeName.toLowerCase() + '-lemon');
    if (lemonCheckbox && lemonCheckbox.checked) {
        toppings.push({ name: 'Lemon', price: 12.50 });
        price += 12.50;
    }
    let mintCheckbox = document.getElementById(coffeeName.toLowerCase() + '-mint');
    if (mintCheckbox && mintCheckbox.checked) {
        toppings.push({ name: 'Mint', price: 25.00 });
        price += 25.00; 
    }

    let quantity = parseInt(document.getElementById(coffeeName.toLowerCase() + '-quantity').value);

    let cartItem = {
        name: coffeeName,
        size: size,
        price: price * quantity,
        toppings: toppings,
        quantity: quantity
    };
    cartItems.push(cartItem);
    updateCart();
}

function updateCart() {
    let cartItemsHTML = '';
    let totalPrice = 0;
    cartItems.forEach((item, index) => {
        cartItemsHTML += `<div class="cart-item" data-index="${index}">${item.quantity}x ${item.name} - `;
        if (item.toppings.length > 0) {
            let toppingsList = item.toppings.map(topping => `${topping.name} (+₱${topping.price.toFixed(2)})`).join(', ');
            cartItemsHTML += `(${toppingsList}) - `;
        }
        cartItemsHTML += `₱${item.price.toFixed(2)} <button onclick="removeFromCart(${index})" style="padding: 3px 8px; font-size: 12px;">Remove</button></div>`;
        totalPrice += item.price;
    });
    document.getElementById('cart-items').innerHTML = cartItemsHTML;
    document.getElementById('cart-total').textContent = totalPrice.toFixed(2);
}

function removeFromCart(index) {
    cartItems.splice(index, 1);
    updateCart();
}

function resetCart() {
    cartItems = [];
    updateCart();
}

function checkout() {
    // Here you can add your logic to handle the checkout process, like redirecting to a payment page or displaying a confirmation message.
    alert('Thank you for your purchase!');
    cartItems = []; // Clear cart after checkout
    updateCart();
}