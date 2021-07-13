 
from django.contrib import admin
from api.models import Restraunt, Customers, Employee, Food, FoodDetail,Bill, BillDetails, RestrauntAccount, RestrauntBank, CustomerRequest, EmploySalary, EmployeeBank
# Register your models here.


admin.site.register(Restraunt)
admin.site.register(Food)
admin.site.register(FoodDetail)
admin.site.register(Employee)
admin.site.register(Customers)
admin.site.register(Bill)
admin.site.register(EmploySalary)
admin.site.register(BillDetails)
admin.site.register(CustomerRequest)
admin.site.register(RestrauntAccount)
admin.site.register(RestrauntBank)
admin.site.register(EmployeeBank)

 