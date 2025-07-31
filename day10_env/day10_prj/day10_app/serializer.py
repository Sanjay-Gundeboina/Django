from rest_framework import serializers
from .models import CAR

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=CAR
        fields=['car_id','car_name','car_model']