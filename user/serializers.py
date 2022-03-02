from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'