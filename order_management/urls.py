from django.urls import path
from .views import OrderCreateView, OrderDetailView, OrderListView

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order-create'),
    path('list/', OrderListView.as_view(), name='order-list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

]
