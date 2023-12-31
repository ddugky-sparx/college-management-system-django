"""
URL configuration for college_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('designation-edit/<int:item_id>/',views.designation_edit,name="designation-edit"),
   path('designation-data/',views.designation_data,name="designation-data"),
   path('designation-add/',views.designation_add,name="designation-add"),
   path('designation-data/<int:item_id>/', views.designation_delete, name="designation-delete"),
   path('qualification-edit/<int:item_id>/',views.qualification_edit,name="qualification-edit"),
   path('qualification-data/',views.qualification_data,name="qualification-data"),
   path('qualification-add/',views.qualification_add,name="qualification-add"),
   path('qualification-data/<int:item_id>/', views.delete, name="qualification-dlete")

   
]
