from django.db import models
from product_management.models import Product

from user_management.models import CustomUser

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
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='PENDING')
    assignment = models.OneToOneField(OrderAssignment, null=True, blank=True, on_delete=models.SET_NULL, related_name='order_assignment')


    def __str__(self):
        return f"Order #{self.id} - {self.user.email}"
