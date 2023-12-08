from django.shortcuts import render,redirect
from master.models import Qualification,Designation
# Create your views here.
def designation_data(request):
    data=Designation.objects.all()
    return render(request,'designation_data.html',{"data":data})


def designation_edit(request,item_id):
    if request.POST:
        edesignation=request.POST['designationedit']
        ecode=request.POST['designationcode']
        status=request.POST['status']
        status_value=status=='1'
        obj= Designation.objects.get(id=item_id)
        obj.designation = edesignation
        obj.code=ecode
        obj.is_active=status_value
        obj.save()
        return redirect('designation-data')  
    else:
        data=Designation.objects.get(id=item_id)
        return render(request,'designation_edit.html',{"data":data})

def designation_add(request):
    if request.method == 'POST':
        designation_name = request.POST['designation']
        designation_code = request.POST['code']
        existing_designation = Designation.objects.filter(designation=designation_name).exists()
        if existing_designation:
            message = "Qualification already exists."
        else:
            new_designation = Designation(designation=designation_name,code=designation_code)
            new_designation.save()
            message = "Submitted"
        return render(request, 'designation_add.html', {"message": message})
    else:
        return render(request, 'designation_add.html')
def designation_delete(request,item_id):
    q = Designation.objects.get(id=item_id)
    q.delete()
    return redirect('designation-data')






def qualification_data(request):
    data=Qualification.objects.all()
    return render(request,'qualification_data.html',{"data":data})

from django.contrib import messages

def qualification_edit(request, item_id):
    if request.method == 'POST':
        ename = request.POST['qualificationedit']
        status = request.POST['status']
        status_value = status == '1'
        existing_qualification = Qualification.objects.exclude(id=item_id).filter(name=ename)
        if existing_qualification.exists():
            data = Qualification.objects.get(id=item_id)
            return render(request, 'qualification_edit.html', {"message":"already exists","data": data})
        obj = Qualification.objects.get(id=item_id)
        obj.name = ename
        obj.is_active = status_value
        obj.save()
        return redirect('qualification-data')  
    else:
        data = Qualification.objects.get(id=item_id)
        return render(request, 'qualification_edit.html', {"data": data})


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