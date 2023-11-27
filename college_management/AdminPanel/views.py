from django.shortcuts import render

# Create your views here.
def adminpanel(request):
   return render(request,'login.html')

def change_password(request):
   return render(request,'change_password.html')
    