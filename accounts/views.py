from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def loginCustomer(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("store") #user goes to store after successful login
        else:
            return render(request, 'index.html', {'error': 'Invalid username or password'})
            print("Login failed!")
    else:
        return render(request, 'index.html')
    
def signupCustomer(request):        
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("landing") #user goes to homepage for login
    else:
        form = UserCreationForm()
        
    return render(request, "signup.html", {'form': form})

def logoutCustomer(request):
    if request.user != None:
        logout(request)
        
    return redirect("landing")