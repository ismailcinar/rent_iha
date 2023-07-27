# serializers.py
from rest_framework import serializers
from ..models import UAV, RentalRecord

class UAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = UAV
        fields = '__all__'

class RentalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalRecord
        fields = '__all__'
