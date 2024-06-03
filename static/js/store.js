// JavaScript for handling the cart modal and adding items to the cart

document.addEventListener('DOMContentLoaded', function() {
    var cartModal = document.getElementById("cartModal");
    var viewCartBtn = document.getElementById("viewCartBtn");
    var closeBtn = document.getElementsByClassName("close")[0];

    viewCartBtn.onclick = function() {
        cartModal.style.display = "block";
    }

    closeBtn.onclick = function() {
        cartModal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == cartModal) {
            cartModal.style.display = "none";
        }
    }

    document.querySelectorAll('.add-to-cart-form').forEach(form => {
        form.onsubmit = function(event) {
            event.preventDefault();

            var formData = new FormData(form);
            fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                updateCartModal();
            })
            .catch(error => console.error('Error:', error));
        }
    });
});

function updateCartModal() {
    fetch('/cart/')
        .then(response => response.text())
        .then(html => {
            document.querySelector('.modal-content').innerHTML = html;
        });
}
