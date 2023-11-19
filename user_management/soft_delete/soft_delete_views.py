from rest_framework import  status
from rest_framework.response import Response
from order_management.models import Order
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class CustomerProfileDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user

        # Check if the user has pending orders
        if Order.objects.filter(user=user, is_pending=True).exists():
            return Response({'detail': 'Cannot delete profile with pending orders.'}, status=status.HTTP_400_BAD_REQUEST)

        user.is_deleted = True
        user.is_active = False 
        user.save()
        # Soft delete the user profile

        user.delete()
        # Log out the user
        Token.objects.filter(user=user).delete()

        return Response({'detail': 'Profile deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)