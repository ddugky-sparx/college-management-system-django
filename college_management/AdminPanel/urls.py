from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import PasswordChangeView
from . import views

urlpatterns = [
   path('Admin-login/',views.adminpanel),
   path('Admin-change/',views.change_password,name="change_password"),
   path('accounts/password_change/', PasswordChangeView.as_view(template_name='change_password.html'), name='password_change'),
   path("accounts/", include("django.contrib.auth.urls")),
   
   
   
]