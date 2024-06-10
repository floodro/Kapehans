from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def loginCustomer(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            print("Login successful!")
            return redirect("menu")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'index.html')

def signupCustomer(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if password == confirm_password:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            user.save()
            print("Data successfully saved!")
            return redirect('landing')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'index.html')

def logoutCustomer(request):
    logout(request)
    # Redirect to some page after logout (e.g., login page)
    return redirect('loginCustomer')
