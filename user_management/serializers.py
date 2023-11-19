from django.contrib.auth import authenticate

from rest_framework import serializers
from .models import CustomUser
import re


class BaseUserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    phone_number = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'password', 'confirm_password', 'phone_number']

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        phone_number = data.get('phone_number')

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")

        # Check for minimum password length
        min_password_length = 6
        if len(password) < min_password_length:
            raise serializers.ValidationError(f"Password must be at least {min_password_length} characters long.")

        # Phone number validation
        if not re.match("^[0-9]+$", phone_number) or len(phone_number) != 10:
            raise serializers.ValidationError("Invalid phone number. It should contain only numeric characters and have exactly 10 digits.")

        return data
    def create(self, validated_data, **extra_fields):
        validated_data.pop('confirm_password', None)
        password = validated_data.pop('password', None)

        user = CustomUser.objects.create_user(**validated_data, **extra_fields)

        if password:
            user.set_password(password)
            user.save()

        return user


class CustomerRegisterSerializer(BaseUserRegisterSerializer):
    class Meta(BaseUserRegisterSerializer.Meta):
        fields = BaseUserRegisterSerializer.Meta.fields + ['is_customer']

    def create(self, validated_data):
        is_delivery_agent = validated_data.pop('is_customer', False)
        return super().create(validated_data, is_customer=True)

class DeliveryAgentRegisterSerializer(BaseUserRegisterSerializer):
    class Meta(BaseUserRegisterSerializer.Meta):
        fields = BaseUserRegisterSerializer.Meta.fields + ['is_delivery_agent']

    def create(self, validated_data):
        is_delivery_agent = validated_data.pop('is_delivery_agent', False)
        return super().create(validated_data, is_delivery_agent=True)
    
class CustomUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)

            if user:
                data['user'] = user
            else:
                raise serializers.ValidationError('Unable to log in with provided credentials.')
        else:
            raise serializers.ValidationError('Must include "email" and "password".')

        return data
    
