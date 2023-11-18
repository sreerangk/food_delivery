from django.urls import path

from user_management.views import UserLoginView, CustomerRegistrationView,DeliveryAgentRegistrationView, block_user, unblock_user


urlpatterns = [
    path('register/customer/', CustomerRegistrationView.as_view(), name='customer-register'),
    path('register/delivery-agent/', DeliveryAgentRegistrationView.as_view(), name='delivery-agent-register'),   

    path('login/', UserLoginView.as_view(), name='user-login'),
    
    path('block/', block_user, name='block_user'),
    path('unblock/', unblock_user, name='unblock_user'),

]