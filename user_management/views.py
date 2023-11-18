from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer, CustomerRegisterSerializer, DeliveryAgentRegisterSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


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