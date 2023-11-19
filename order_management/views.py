from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from product_management.permissions import IsAdmin
from .models import Order
from .serializers import OrderSerializer
from django.utils.datastructures import MultiValueDict
from django.utils import timezone
from rest_framework import generics, permissions, status

from rest_framework.serializers import ValidationError
from .models import OrderAssignment
from .serializers import OrderAssignmentSerializer

class IsOrderOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an order to view or cancel it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        # Create a mutable copy of the QueryDict
        mutable_data = MultiValueDict(request.data.copy())

        # Set the user as the currently logged-in user
        mutable_data['user'] = request.user.id
        mutable_data['is_pending'] = True

        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retrieve orders for the logged-in user
        return Order.objects.filter(user=self.request.user)
    

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsOrderOwner]
    queryset = Order.objects.all()

    def perform_update(self, serializer):
        # Check if the order is within 30 minutes of creation for cancellation
        order = self.get_object()
        if (timezone.now() - order.created_at).seconds < 1800:
            serializer.save(status='CANCELLED')
            order.is_pending = False
            order.save()
        else:
            # Order cannot be cancelled after 30 minutes
            raise ValidationError("Cannot cancel order after 30 minutes of creation")

    def perform_destroy(self, instance):
        if (timezone.now() - instance.created_at).seconds < 1800: 
            instance.status = 'CANCELLED'
            instance.is_pending = False
            instance.save()
        else:
            raise ValidationError("Cannot cancel order after 30 minutes of creation")
        
        
class OrderAssignmentListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderAssignmentSerializer
    permission_classes = [IsAdmin]

    def get_queryset(self):
        # Only show the list of assigned orders
        return OrderAssignment.objects.filter(delivery_agent__isnull=False)

class OrderAssignmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderAssignment.objects.all()
    serializer_class = OrderAssignmentSerializer
    permission_classes = [IsAdmin]
