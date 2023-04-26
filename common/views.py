from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
# Create your views here.
class GetItemwithCategoryView(APIView):
    def get(self, request, format=None):
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)



class GetDATruckListView(APIView):
    def get(self, request, format=None):
        datruck = DATruckList.objects.all()
        serializer = DATruckListSerializer(datruck, many=True)
        return Response(serializer.data)


