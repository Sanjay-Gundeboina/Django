from rest_framework import serializers
from .models import DJANGO_USERS

class DJANGO_USER_SERIALIZER(serializers.ModelSerializer):
    class Meta:
        model=DJANGO_USERS
        fields="__all__"