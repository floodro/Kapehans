from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

# Create your views here.
def loginCustomer(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password'] 
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(user)
            return redirect("dashboard")
        
        else:
            messages.info(request, "Username or password is incorrect")