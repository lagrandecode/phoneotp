from rest_framework import serializers 
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password','isVerified']


class VerifySerializer(serializers.Serializer):
    phone_number = serializers.EmailField()
    otp = serializers.CharField()