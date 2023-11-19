
from rest_framework import serializers

from order_management.models import Order, OrderAssignment
from user_management.models import CustomUser


class OrderAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderAssignment
        fields = '__all__'


class UpdateOrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']
        

class OTPConfirmationSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    otp = serializers.CharField(max_length=6)