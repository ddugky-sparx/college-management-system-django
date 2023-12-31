from django.shortcuts import render,redirect
from master.models import Designation,Qualification
from .models import Employee

# Create your views here.
def employees_data(request):
    visited=int(request.COOKIES.get("visit",0))
    visited+=1
    employee = Employee.objects.all()
    response=render(request,'employees_data.html',{"data":employee,"visited":visited})
    response.set_cookie("visit",visited)
    return response

def employees_register(request):
   
    if request.method == 'POST':
        # Extract data from POST request
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        locality = request.POST.get('Locality')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        qualification_id = request.POST.get('qualification')
        designation_id = request.POST.get('designation')
        salary_amount = request.POST.get('snumber')
        salary_day = request.POST.get('salary_day')
        joining_date = request.POST.get('jdate')
        image_file = request.FILES['photo']
        
        
        qobj= Qualification.objects.get(id=qualification_id)
        dobj=Designation.objects.get(id=designation_id)
        # Create Employee object
        employee = Employee.objects.create(
            fname=fname,
            lname=lname,
            email=email,
            locality=locality,
            dob=dob,
            phone=phone,
            gender=gender,
            qualification=qobj,
            designation=dobj,
            salary_amount=salary_amount,
            salary_day=salary_day,
            joining_date=joining_date,
            image=image_file
        )
        response=render(request,"employees_data.html",{"data":employee})
        return response
    
    ddata=Designation.objects.filter(is_active=True)
    qdata=Qualification.objects.filter(is_active=True)
    return render(request,'employees_register.html',{"ddata":ddata,"qdata":qdata})