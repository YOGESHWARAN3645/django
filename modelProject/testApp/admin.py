from django.contrib import admin
from testApp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):                       #u need to know
    list_display=['name',"employee_Id","employee_salary"]

admin.site.register(Employee,EmployeeAdmin) 

# Register your models here.
