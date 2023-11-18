from rest_framework.response import Response
from rest_framework import status

from product_management.permissions import IsAdminOrReadOnly
from .serializers import CustomUserSerializer, CustomerRegisterSerializer, DeliveryAgentRegisterSerializer, UserBlockSerializer, UserUnblockSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from .models import CustomUser


class CustomerRegistrationView(APIView):
    serializer_class = CustomerRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        response_data = {
            'message': 'Customer registered successfully',
            'user_id': user.id,
            'email': user.email,
            'phone_number': user.phone_number,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_customer': user.is_customer,
            'is_blocked': user.is_blocked,
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

class DeliveryAgentRegistrationView(APIView):
    serializer_class = DeliveryAgentRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        response_data = {
            'message': 'Delivery agent registered successfully',
            'user_id': user.id,
            'email': user.email,
            'phone_number': user.phone_number,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_delivery_agent': user.is_delivery_agent,
            'is_blocked': user.is_blocked,
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=status.HTTP_200_OK)
    

@api_view(['POST'])
@permission_classes([IsAdminOrReadOnly])
def block_user(request):
    serializer = UserBlockSerializer(data=request.data)
    if serializer.is_valid():
        user_id = serializer.validated_data['user_id']
        user = get_object_or_404(CustomUser, id=user_id)
        user.block_user()
        return Response({'status': 'success', 'message': 'User blocked successfully'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminOrReadOnly])
def unblock_user(request):
    serializer = UserUnblockSerializer(data=request.data)
    if serializer.is_valid():
        user_id = serializer.validated_data['user_id']
        user = get_object_or_404(CustomUser, id=user_id)
        user.unblock_user()
        return Response({'status': 'success', 'message': 'User unblocked successfully'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)