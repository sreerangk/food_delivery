

from django.urls import path

from user_management.views import UserLoginView, CustomerRegistrationView,DeliveryAgentRegistrationView


urlpatterns = [
    path('register/customer/', CustomerRegistrationView.as_view(), name='customer-register'),
    path('register/delivery-agent/', DeliveryAgentRegistrationView.as_view(), name='delivery-agent-register'),    path('login/', UserLoginView.as_view(), name='user-login'),
    path('login/', UserLoginView.as_view(), name='user-login'),

]