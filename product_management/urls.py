from django.urls import path
from .views import ProductCreateView, ProductDeleteView, ProductListCreateView, ProductDetailView

urlpatterns = [
    path('list/', ProductListCreateView.as_view(), name='product-list-create'),
    path('edit/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),

]
