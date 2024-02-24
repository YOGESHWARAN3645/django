from django.shortcuts import render
from testApp.models import Employee
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
'''from faker import Faker'''


def employee_details(request):
    employee_list = Employee.objects.all()
    send_dict = {'employee_list':employee_list}
    return render(request,'testApp/Employee.html',context=send_dict)


class userApiView(APIView):
    def get(self,request):
        allUsers = Employee.objects.all().values()
        return Response({"messages":"list of users","user list":allUsers})
        
    def post(self,request):
        Employee.objects.create(
            name=request.data["name"], 
            employee_Id= request.data["employee_Id"], 
            employee_salary=request.data["employee_salary"], 
            date_of_birth=request.data["date_of_birth"], 
            nature_of_employement=request.data["nature_of_employement"], 
            blood_group=request.data["blood_group"], 
            email=request.data["email"], 
            phone_number=request.data["phone_number"], 
            address=request.data["address"])
        return Response({"messages":"NewBook Added","user":user})   

# Create your views here.
'''
def fake_list(request)
    fake_employee_list = Faker()

    for i in range(3):
        name= fake_employee_list.name()
        employee_Id = fake_employee_list.random_int(min=1000,max=9999)
        employee_salary = fake_employee_list.random_int(min= 10000,max=100000)
        date_of_birth = fake_employee_list.date_of_birth()
        nature_of_employement = fake_employee_list.random_element(elements=("Staff' ","operator", "Labour"))
        blood_group = fake_employee_list.random_element(elements=('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'))
        email = fake_employee_list.email()
        phone_number = fake_employee_list.phone_number()
        address = fake_employee_list.address()
        employee_record = Employee.objects.Create(name=name,employee_Id=employee_Id,employee_salary=employee_salary,date_of_birth=date_of_birth,nature_of_employement=nature_of_employement,blood_group=blood_group,email=email,phone_number=phone_number,address=address)
        employee_record.save()
'''