from django.shortcuts import render
from django.shortcuts import redirect
from master.models import Qualification
# Create your views here.
def designation_data(request):
    return render(request,'designation_data.html',{"name":"shameel"})

def designation_edit(request):
    return render(request,'designation_edit.html')

def designation_add(request):
    return render(request,'designation_add.html')

def qualification_data(request):
    data=Qualification.objects.all()
    return render(request,'qualification_data.html',{"data":data})

def qualification_edit(request,item_id):
    if request.POST:
        ename=request.POST['qualificationedit']
        status=request.POST['status']
        print(type(status=='1'))
        obj= Qualification.objects.get(id=item_id)
        obj.name = ename
        obj.save()
        return redirect('qualification-data')  
    else:
        data=Qualification.objects.get(id=item_id)
        return render(request,'qualification_edit.html',{"data":data})


from django.shortcuts import render, redirect
from .models import Qualification

def qualification_add(request):
    if request.method == 'POST':
        qualification_name = request.POST['qualification']
        existing_qualification = Qualification.objects.filter(name=qualification_name).exists()
        if existing_qualification:
            message = "Qualification already exists."
        else:
            new_qualification = Qualification(name=qualification_name)
            new_qualification.save()
            message = "Submitted"
        return render(request, 'qualification_add.html', {"message": message})
    else:
        return render(request, 'qualification_add.html')

def delete(request,item_id):
    q = Qualification.objects.get(id=item_id)
    q.delete()
    return redirect('qualification-data')
    
    

# def dummy(request):
#     # print(request.POST['qualification'])
#     qualification=request.POST['qualification']
#     return render(request,'dummy.html',{'iteam':qualification})