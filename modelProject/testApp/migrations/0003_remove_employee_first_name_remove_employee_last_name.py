# Generated by Django 5.0.1 on 2024-02-24 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0002_employee_address_employee_blood_group_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_name',
        ),
    ]