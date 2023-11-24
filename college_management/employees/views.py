from django.shortcuts import render

# Create your views here.
def employees_data(request):
    return render(request,'employees_data.html')
def employees_register(request):
    return render(request,'employees_register.html')