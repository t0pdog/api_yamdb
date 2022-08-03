from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
    """Доступ только Администратор."""

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return (request.user.access_administrator
                    or request.user.is_superuser)
        return False
