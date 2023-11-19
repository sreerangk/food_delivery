from django.urls import path

from order_management.order_placement.oreder_delivery import OTPConfirmationView, OrderDeliveryView, UpdateOrderStatusView
from .views import OrderAssignmentListCreateView, OrderAssignmentRetrieveUpdateDestroyView, OrderCreateView, OrderDetailView, OrderListView

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order-create'),
    path('list/', OrderListView.as_view(), name='order-list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

    path('admin/order-assignment/', OrderAssignmentListCreateView.as_view(), name='order-Assignment'),
    path('admin/order-assignment/<int:pk>/', OrderAssignmentRetrieveUpdateDestroyView.as_view(), name='order-assignment-detail'),

    path('agent/delivery/', OrderDeliveryView.as_view(), name='agent-delivery'),
    path('agent/update/<int:pk>/', UpdateOrderStatusView.as_view(), name='update-order-status'),
    path('agent/otp-confirmation/<int:pk>/', OTPConfirmationView.as_view(), name='otp-confirmation'),

]
