# views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from order_management.models import Order, OrderAssignment
from order_management.order_placement.serializer import OTPConfirmationSerializer, OrderAssignmentSerializer, UpdateOrderStatusSerializer
from product_management.permissions import IsDeliveryAgent


class OrderDeliveryView(generics.ListAPIView):
    queryset = OrderAssignment.objects.all()
    serializer_class = OrderAssignmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsDeliveryAgent]
    def get_queryset(self):
        # Filter orders based on the logged-in delivery agent
        return OrderAssignment.objects.filter(delivery_agent=self.request.user)
  
class UpdateOrderStatusView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = UpdateOrderStatusSerializer
    permission_classes = [permissions.IsAuthenticated, IsDeliveryAgent]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # Use the provided status from the request data
        status = request.data.get('status')
        if status:
            instance.status = status
            instance.save()

        return Response(self.get_serializer(instance).data)
    
    

class OTPConfirmationView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OTPConfirmationSerializer
    permission_classes = [permissions.IsAuthenticated,IsDeliveryAgent]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check if the provided OTP matches the saved OTP
        if instance.otp == serializer.validated_data['otp']:
            instance.status = 'CONFIRM-DELIVERED'
            instance.save()

            return Response({'detail': 'Delivery confirmed successfully.'})
        else:
            return Response({'detail': 'Invalid OTP.'}, status=400)