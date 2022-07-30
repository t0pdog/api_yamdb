from rest_framework import permissions


class IsOwnerOnly(permissions.BasePermission):
    """Доступ только владелец учетной записи."""
    
    def has_permission(self, request, view):
        return request.user.is_authenticated


class AdminOnly(permissions.BasePermission):
    """Доступ только Администратор."""

    def has_permission(self, request, view):
        return('admin' == request.user.role or request.user.is_superuser)
