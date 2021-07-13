from rest_framework import serializers
from api.models import Company

class CompanySerializers(serializers.HyperlinkedModelSerializer):
  class meta:
      model=Company
      fields=["name","license_no","address","contact_no","email"]
