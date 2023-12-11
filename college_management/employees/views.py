from django.shortcuts import render
from master.models import Designation,Qualification

# Create your views here.
def employees_data(request):
    return render(request,'employees_data.html')
def employees_register(request):
    ddata=Designation.objects.filter(is_active=True)
    qdata=Qualification.objects.filter(is_active=True)
    return render(request,'employees_register.html',{"ddata":ddata,"qdata":qdata})