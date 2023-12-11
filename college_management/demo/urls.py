from django.urls import path
from demo import views


urlpatterns = [
  path('demo/',views.create_product ),
  path('show/',views.show ),


]