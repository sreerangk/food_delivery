from rest_framework.response import Response
from rest_framework import status

from product_management.permissions import IsAdmin
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from user_management.models import CustomUser
from user_management.user_block_and_unblock.serializers import UserBlockSerializer, UserUnblockSerializer



@api_view(['POST'])
@permission_classes([IsAdmin])
def block_user(request):
    serializer = UserBlockSerializer(data=request.data)
    if serializer.is_valid():
        user_id = serializer.validated_data['user_id']
        user = get_object_or_404(CustomUser, id=user_id)
        user.block_user()
        return Response({'status': 'success', 'message': 'User blocked successfully'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdmin])
def unblock_user(request):
    serializer = UserUnblockSerializer(data=request.data)
    if serializer.is_valid():
        user_id = serializer.validated_data['user_id']
        user = get_object_or_404(CustomUser, id=user_id)
        user.unblock_user()
        return Response({'status': 'success', 'message': 'User unblocked successfully'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)