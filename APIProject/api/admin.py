 
from django.contrib import admin
from api.models import Company, Customers, Employee, Food, FoodDetail,Bill, BillDetails, CompanyAccount, CompanyBank, CustomerRequest, EmploySalary, EmployeeBank
# Register your models here.


admin.site.register(Company)
admin.site.register(Food)
admin.site.register(FoodDetail)
admin.site.register(Employee)
admin.site.register(Customers)
admin.site.register(Bill)
admin.site.register(EmploySalary)
admin.site.register(BillDetails)
admin.site.register(CustomerRequest)
admin.site.register(CompanyAccount)
admin.site.register(CompanyBank)
admin.site.register(EmployeeBank)

 