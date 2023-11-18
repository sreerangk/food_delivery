from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['user'] 

    def create(self, validated_data):
        # Set the 'user' field to the currently logged-in user
        validated_data['user'] = self.context['request'].user
        return super(OrderSerializer, self).create(validated_data)
    
    