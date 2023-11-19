from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from product_management.permissions import IsAdmin
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdmin]

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdmin]
    

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdmin]

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdmin]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        product_id = instance.id
        self.perform_destroy(instance)
        return Response({'message': f'Product with ID {product_id} deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)