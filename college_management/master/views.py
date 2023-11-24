from django.shortcuts import render

# Create your views here.
def designation_data(request):
    return render(request,'designation_data.html')

def designation_edit(request):
    return render(request,'designation_edit.html')

def designation_add(request):
    return render(request,'designation_add.html')

def qualification_data(request):
    return render(request,'qualification_data.html')

def qualification_edit(request):
    return render(request,'qualification_edit.html')

def qualification_add(request):
    return render(request,'qualification_add.html')