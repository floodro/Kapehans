from django.urls import path
from . import views

urlpatterns = [
    path("", views.landingPage, name="landing"),
    path("store/", views.storePage, name="store"),
    path("about/", views.aboutUs, name="about"),
    path("contact/", views.contactUs, name="contact"),
    path("reviews/", views.reviews, name="reviews")
]


