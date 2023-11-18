from django.contrib import admin

from order_management.models import Order, OrderAssignment
from user_management.models import CustomUser

# Register your models here.

class OrderAssignmentAdmin(admin.ModelAdmin):
    list_display = ['order', 'delivery_agent', 'assigned_at']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'delivery_agent':
            # Filter the queryset to only include CustomUser instances with is_delivery_agent=True
            kwargs['queryset'] = CustomUser.objects.filter(is_delivery_agent=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(OrderAssignment, OrderAssignmentAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_amount', 'payment_method', 'created_at', 'status']

    actions = ['mark_as_assigned']

    def mark_as_assigned(self, request, queryset):
        # Custom admin action to mark selected orders as ASSIGNED
        for order in queryset:
            order.status = 'ASSIGNED'
            # You may also create an OrderAssignment instance here if needed
            order.save()

    mark_as_assigned.short_description = "Mark selected orders as ASSIGNED"

admin.site.register(Order, OrderAdmin)