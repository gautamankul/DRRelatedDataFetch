from rest_framework import serializers
from .models import *



# Create serializers here..

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    


  

class ItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')

    class Meta:
        model = Item
        fields = ('id', 'name', 'category_name')


class TruckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckList
        fields = '__all__'


class DispatchAdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatchAdvice
        fields = '__all__'


# create a serializer for DATruckList to get all record along with TruckList  and DispatchAdvice 
class DATruckListSerializer(serializers.ModelSerializer):
    truck_list_name = serializers.CharField(source='truckListID.vehicle_no')
    dispatch_advice = serializers.CharField(source='daID.jobcode_da_no')

    class Meta:
        model = DATruckList
        fields = ('id','created_by', 'truck_list_name', 'dispatch_advice')
