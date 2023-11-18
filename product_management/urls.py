from django.urls import path
from .views import ProductCreateView, ProductListCreateView, ProductDetailView

urlpatterns = [
    path('list/', ProductListCreateView.as_view(), name='product-list-create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('create/', ProductCreateView.as_view(), name='product-create'),

]
