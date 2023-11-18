from rest_framework import serializers

from user_management.models import CustomUser
from .models import Order, OrderAssignment

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['user'] 

    def create(self, validated_data):
        # Set the 'user' field to the currently logged-in user
        validated_data['user'] = self.context['request'].user
        return super(OrderSerializer, self).create(validated_data)
    
    
class OrderAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderAssignment
        fields = ['id', 'order', 'delivery_agent', 'assigned_at']
        read_only_fields = ['id']
        extra_kwargs = {
            'delivery_agent': {'queryset': CustomUser.objects.filter(is_delivery_agent=True)}
        }