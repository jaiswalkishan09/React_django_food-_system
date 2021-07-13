
from rest_framework import serializers
from api.models import Restraunt,RestrauntBank,Food,FoodDetail,Employee,Customers,Bill,CustomerRequest,RestrauntAccount,EmployeeBank,EmploySalary,BillDetails

class RestrauntSerializers(serializers.HyperlinkedModelSerializer):
  class Meta:
      model=Restraunt
      fields=["name","license_no","address","contact_no","email"]

class RestrauntBankSerializer(serializers.ModelSerializer):
    class Meta:
        model=RestrauntBank
        fields="__all__"


class FoodSerliazer(serializers.ModelSerializer):
    class Meta:
        model=Food
        fields="__all__"

    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['restraunt']=RestrauntSerializers(instance.restraunt_id).data
        return response

class FoodDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=FoodDetail
        fields="__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Food'] = FoodSerliazer(instance.food_id).data
        return response

class FoodDetailsSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model=FoodDetail
        fields="__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields="__all__"

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bill
        fields="__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['customer'] = CustomerSerializer(instance.customer_id).data
        return response

class CustomerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerRequest
        fields="__all__"


class RestrauntAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=RestrauntAccount
        fields="__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['restraunt'] = RestrauntSerializers(instance.restraunt_id).data
        return response


class EmployeeBankSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeBank
        fields="__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['employee'] = EmployeeSerializer(instance.employee_id).data
        return response


class EmployeeSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model=EmploySalary
        fields="__all__"

class BillDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=BillDetails
        fields="__all__"