from django.db import models
from django.utils import timezone


class Employee(models.Model):
    name= models.CharField(max_length=50,default='')
    employee_Id = models.CharField(max_length=1000,default='')
    employee_salary = models.CharField(max_length=1000,default='')
    date_of_birth = models.DateField(default=timezone.now)
    nature_of_employement = models.CharField(max_length=1000,default='')
    blood_group = models.CharField(max_length=3,default='')
    email = models.EmailField(default='')
    phone_number = models.CharField(max_length=1000,default='')
    address = models.CharField(max_length=100000,default='Unknown')
    def __str__(self): 
        return 'Employee Object with eno: +str(self.no)' #u need to know