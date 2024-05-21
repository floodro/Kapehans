const form = document.getElementById('contact-form');
const messageSent = document.getElementById('message-sent');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  // Basic form validation (more can be added)
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const message = document.getElementById('message').value;

  if (name === '' || email === '' || message === '') {
    messageSent.textContent = 'Please fill out all required fields.';
    return;
  }

  // Simulate sending message (replace with actual functionality)
  messageSent.textContent = 'Your message has been sent!';
  form.reset();
});

document.querySelector("#show-login").addEventListener("click", function(){
  document.querySelector(".popup").classList.add("active");
});
document.querySelector(".popup .close-btn") .addEventListener("click" , function(){
  document.querySelector(".popup").classList.remove("active");
});