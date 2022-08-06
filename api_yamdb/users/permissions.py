from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
    """Доступ только Администратор."""

    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and (request.user.access_administrator
                     or request.user.is_superuser))
