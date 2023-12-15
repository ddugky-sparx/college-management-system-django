
from django.urls import path
from . import views

urlpatterns = [
    path("employees-data/",views.employees_data,name="employees-data"),
    path("employees-register/",views.employees_register)
]
