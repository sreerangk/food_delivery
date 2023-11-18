from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin access the view.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsDeliveryAgent(permissions.BasePermission):
    """
    Custom permission to only allow delivery agents to access the view.
    """

    def has_permission(self, request, view):
        # Check if the user has the role of a delivery agent
        return request.user and request.user.is_authenticated and request.user.is_delivery_agent
