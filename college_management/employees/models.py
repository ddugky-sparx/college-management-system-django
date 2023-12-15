from django.db import models
from master.models import Designation,Qualification

# Create your models here.
class Employee(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    locality = models.TextField()
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=20)
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    salary_amount = models.DecimalField(max_digits=10, decimal_places=2)
    salary_day = models.PositiveIntegerField()
    joining_date = models.DateField()