
from django.urls import path
from . import views

urlpatterns = [
    path("employees-data/",views.employees_data),
    path("employees-register/",views.employees_register)
]
