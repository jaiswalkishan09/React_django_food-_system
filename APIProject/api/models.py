from os import name
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Company(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    license_no=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    contact_no=models.CharField(max_length=255)
    email=models.CharField(max_length=254)
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Food(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    Food_type=models.CharField(max_length=255)
    sell_price=models.CharField(max_length=255)
    company_id=models.ForeignKey(Company,on_delete=models.CASCADE)
    Available=models.BooleanField(blank=True)
    objects=models.Manager()

class FoodDetail(models.Model):
    id=models.AutoField(primary_key=True)
    food_id=models.ForeignKey(Food,on_delete=CASCADE)
    description=models.CharField( max_length=255)
    objects=models.Manager()

class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    join_date=models.DateField()
    phone=models.CharField(max_length=255)
    adress=models.CharField(max_length=255)
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
   

class Customers(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    adress=models.CharField(max_length=255)
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Bill(models.Model):
    id=models.AutoField(primary_key=True)
    Customers_id=ForeignKey(Customers,on_delete=models.CASCADE)   
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class EmploySalary(models.Model):
    id=models.AutoField(primary_key=True)
    employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    salary_date=models.DateField()
    salary=models.CharField( max_length=255)
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class BillDetails(models.Model):
    id=models.AutoField(primary_key=True)
    bill_id=models.ForeignKey(Bill,on_delete=models.CASCADE)
    food_id=models.ForeignKey(Food,on_delete=models.CASCADE)
    qty=models.IntegerField()
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class CustomerRequest(models.Model):
    id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    Food_details=models.CharField(max_length=255)
    status=models.BooleanField(default=False)
    added_on=models.DateTimeField(auto_now_add=True)
    prescription=models.FileField(default="")
    objects=models.Manager()

class CompanyAccount(models.Model):
    choices=((1,"Debit"),(2,"Credit"))

    id=models.AutoField(primary_key=True)
    company_id=models.ForeignKey(Company,on_delete=models.CASCADE)
    transaction_type=models.CharField(choices=choices,max_length=255)
    transaction_amt=models.CharField(max_length=255)
    transaction_date=models.DateField()
    payment_mode=models.CharField(max_length=255)
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class CompanyBank(models.Model):
    id=models.AutoField(primary_key=True)
    bank_account_no=models.CharField(max_length=255)
    ifsc_no=models.CharField(max_length=255)
    company_id=models.ForeignKey(Company,on_delete=models.CASCADE)
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class EmployeeBank(models.Model):
    id=models.AutoField(primary_key=True)
    bank_account_no=models.CharField(max_length=255)
    ifsc_no=models.CharField(max_length=255)
    employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    added_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
