from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginCustomer, name="loginCustomer"),
    path("signup/", views.signupCustomer, name="signupCustomer"),
    path("logout/", views.logoutCustomer, name="logoutCustomer"),
]

