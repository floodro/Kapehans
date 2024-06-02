document.addEventListener('DOMContentLoaded', () => {
const cartModal = document.getElementById('cartModal');
const viewCartBtn = document.getElementById('viewCartBtn');
const closeModalBtn = document.querySelector('.close');
const cartTableBody = document.querySelector('#cartTable tbody');
const totalPriceElement = document.getElementById('totalPrice');

    viewCartBtn.addEventListener('click', () => {
        cartModal.style.display = 'block';
    });

    closeModalBtn.addEventListener('click', () => {
        cartModal.style.display = 'none';
    });

    window.addEventListener('click', (event) => {
        if (event.target == cartModal) {
            cartModal.style.display = 'none';
        }
    })
})