from django.shortcuts import render, redirect

# Create your views here.
def landingPage(request):
    return render(request, "index.html", {})

def storePage(request):
    return render(request, "store.html", {})

def contactUs(request):
    return render(request, "contact.html", {})

def aboutUs(request):
    return render(request, "about.html", {})

def reviews(request):
    return render(request, "reviews.html", {})