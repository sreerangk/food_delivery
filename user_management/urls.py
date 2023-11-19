from django.urls import path
from user_management.soft_delete.soft_delete_views import CustomerProfileDeleteView
from user_management.user_block_and_unblock.views import block_user, unblock_user

from user_management.views import DeliveryAgentListView, UserLoginView, CustomerRegistrationView,DeliveryAgentRegistrationView


urlpatterns = [
    path('register/customer/', CustomerRegistrationView.as_view(), name='customer-register'),
    path('register/delivery-agent/', DeliveryAgentRegistrationView.as_view(), name='delivery-agent-register'),   

    path('login/', UserLoginView.as_view(), name='user-login'),
    
    path('delivery-agents/', DeliveryAgentListView.as_view(), name='delivery-agent-list'),

    path('block/', block_user, name='block_user'),
    path('unblock/', unblock_user, name='unblock_user'),

    path('profiles/delete/', CustomerProfileDeleteView.as_view(), name='customer-profile-delete'),

]