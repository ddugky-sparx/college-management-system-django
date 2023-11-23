from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def register(request):
    return render(request,'student_regi.html')
def data(request):
    return render(request,'student_data.html')

def student_add(request):
    return render(request,'.html')