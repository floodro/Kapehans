let currentIndex = 0;

function showMenu() {
    document.getElementById("navLinks").style.right = "0";
}

function hideMenu() {
    document.getElementById("navLinks").style.right = "-200px";
}

function moveCarouselOne(direction) {
    const carouselInner = document.querySelector('.carousel-inner');
    const totalItems = carouselInner.children.length;
    currentIndex = (currentIndex + direction + totalItems) % totalItems;
    const offset = -currentIndex * 100;
    carouselInner.style.transform = `translateX(${offset}%)`;
}

document.addEventListener("DOMContentLoaded", function() {
    const menuItems = document.querySelectorAll('.menu-col');

    menuItems.forEach(item => {
        const img = item.querySelector('img');
        if (img && img.src.includes('soldout.jpg')) {
            const button = item.querySelector('.add-to-cart-btn');
            if (button) {
                button.disabled = true;
                button.style.backgroundColor = 'gray'; 
                button.style.cursor = 'not-allowed';
            }
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const messages = document.getElementById('messages');
    if (messages) {
        setTimeout(function() {
            messages.style.display = 'none';
        }, 3000);
    }
});