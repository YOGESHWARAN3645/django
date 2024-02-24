import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','modelProject.settings')
import django 
django.setup()

from testApp.models import Employee
from faker import Faker

fake_employee_list = Faker()

for i in range(1000):
    name= fake_employee_list.name()
    employee_Id = fake_employee_list.random_int(min=1000,max=9999)
    employee_salary = fake_employee_list.random_int(min= 10000,max=100000)
    date_of_birth = fake_employee_list.date_of_birth()
    nature_of_employement = fake_employee_list.random_element(elements=("Staff' ", "operator", "Labour"))
    blood_group = fake_employee_list.random_element(elements=('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'))
    email = fake_employee_list.email()
    phone_number = fake_employee_list.phone_number()
    address = fake_employee_list.address()
    employee_record = Employee.objects.create(name=name, employee_Id=employee_Id, employee_salary=employee_salary, date_of_birth=date_of_birth, nature_of_employement=nature_of_employement, blood_group=blood_group, email=email, phone_number=phone_number, address=address)
    employee_record.save()

