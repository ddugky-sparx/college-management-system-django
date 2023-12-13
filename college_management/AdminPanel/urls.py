from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('Admin-login/',views.adminpanel),
   path('Admin-change/',views.change_password,name="change_password"),
   path("accounts/", include("django.contrib.auth.urls")),
   
]