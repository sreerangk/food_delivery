from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Custom permission to only allow admin access to the view.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsDeliveryAgent(permissions.BasePermission):
    """
    Custom permission to only allow delivery agents to access the view.
    """

    def has_permission(self, request, view):
        # Check if the user has the role of a delivery agent
        return request.user and request.user.is_authenticated and request.user.is_delivery_agent
