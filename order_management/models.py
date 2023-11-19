from django.db import models
from product_management.models import Product

from user_management.models import CustomUser
import random
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
# Create your models here.
    
class OrderAssignment(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    delivery_agent = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Assignment #{self.id} - Order #{self.order.id} to {self.delivery_agent.email}"
    
    
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    PAYMENT_METHOD_CHOICES = [
        ('COD', 'Cash on Delivery'),
        ('Online', 'Online Payment'),
    ]
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES, default='COD')
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CANCELLED', 'Cancelled'),
        ('DELIVERED', 'Delivered'),
        ('CONFIRM-DELIVERED','confirm-delivered')
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='PENDING')
    assignment = models.OneToOneField(OrderAssignment, null=True, blank=True, on_delete=models.SET_NULL, related_name='order_assignment')
    is_pending = models.BooleanField(default=True)
    otp = models.CharField(max_length=6, blank=True)
 
    def send_otp_email(self, otp):
        # Send an email to the user with the OTP
        subject = 'Your OTP for Order #{0}'.format(self.id)
        message = 'Your OTP for Order #{0} is: {1}'.format(self.id, otp)
        send_mail(subject, message, 'helpa077637@gmail.com', [self.user.email])

    def generate_otp(self):
        # Generate a 6-digit OTP
        return str(random.randint(100000, 999999))

    def save(self, *args, **kwargs):
        # Check if the status is being changed to "DELIVERED"
        if self.id and self.status == 'DELIVERED' and self.status != self.__class__.objects.get(id=self.id).status:
            # Generate and set the OTP
            self.otp = self.generate_otp()

            # Additional logic for sending the OTP to the customer
            # You may want to use a notification system or trigger an email here
            self.send_otp_email(self.otp)

        super(Order, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"Order #{self.id} - {self.user.email}"
