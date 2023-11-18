from django.urls import path
from .views import OrderAssignmentListCreateView, OrderAssignmentRetrieveUpdateDestroyView, OrderCreateView, OrderDetailView, OrderListView

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order-create'),
    path('list/', OrderListView.as_view(), name='order-list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

    path('admin/order-assignment/', OrderAssignmentListCreateView.as_view(), name='order-Assignment'),
    path('admin/order-assignment/<int:pk>/', OrderAssignmentRetrieveUpdateDestroyView.as_view(), name='order-assignment-detail'),

]
