from api.serializers import RestrauntSerializers,RestrauntBankSerializer
from django.shortcuts import render

from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.models import Restraunt,RestrauntBank
# Create your views here.

class RestrauntViewSet(viewsets.ViewSet):
   authentication_classes = [JWTAuthentication]
   permission_classes = [IsAuthenticated]
   def list(self,request):
       restraunt=Restraunt.objects.all()
       serializer=RestrauntSerializers(restraunt,many=True,context={"request":request})
       response_dict={"error":False,"message":"All Restraunt List Data","data":serializer.data}
       return Response(response_dict)
  
   def create(self,request):
        try:
            serializer=RestrauntSerializers(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Restraunt Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Restraunt Data"}
        return Response(dict_response)
   def retrieve(self, request, pk=None):
        queryset = Restraunt.objects.all()
        restraunt = get_object_or_404(queryset, pk=pk)
        serializer = RestrauntSerializers(restraunt, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Medicine Details of Current Medicine ID
        restraunt_bank_details = RestrauntBank.objects.filter(restraunt_id=serializer_data["id"])
        restrauntbank_details_serializers = RestrauntBankSerializer(restraunt_bank_details, many=True)
        serializer_data["restraunt_bank"] = restrauntbank_details_serializers.data

        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

   def update(self,request,pk=None):
        try:
            queryset=Restraunt.objects.all()
            restraunt=get_object_or_404(queryset,pk=pk)
            serializer=RestrauntSerializers(restraunt,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated Restraunt Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating Restraunt Data"}

        return Response(dict_response)


class RestrauntBankViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def create(self,request):
        try:
            serializer=RestrauntBankSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Restraunt Bank Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Restraunt Bank Data"}
        return Response(dict_response)

    def list(self,request):
        restrauntbank=RestrauntBank.objects.all()
        serializer=RestrauntBankSerializer(restrauntbank,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Restraunt Bank List Data","data":serializer.data}
        return Response(response_dict)


    def retrieve(self,request,pk=None):
        queryset=RestrauntBank.objects.all()
        restrauntbank=get_object_or_404(queryset,pk=pk)
        serializer=RestrauntBankSerializer(restrauntbank,context={"request":request})
        return Response({"error":False,"message":"Single Data Fetch","data":serializer.data})


    def update(self,request,pk=None):
        queryset=RestrauntBank.objects.all()
        restrauntbank=get_object_or_404(queryset,pk=pk)
        serializer=RestrauntBankSerializer(restrauntbank,data=request.data,context={"request":request})
        serializer.is_valid()
        serializer.save()
        return Response({"error":False,"message":"Data Has Been Updated"})

# restraunt_list=RestrauntViewSet.as_view({"get":"list"})
# restraunt_creat=RestrauntViewSet.as_view({"post":"create"})
# restraunt_update=RestrauntViewSet.as_view({"put":"update"})