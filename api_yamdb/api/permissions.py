from rest_framework import permissions


class IsOwnerUpdate(permissions.BasePermission):
    """Изменения только владельц."""

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsModeratorUpdate(permissions.BasePermission):
    """Изменения только модератор."""

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.access_moderator)


class IsAdminUpdate(permissions.BasePermission):
    """Изменения только администратор."""

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.access_administrator
                or request.user.is_superuser)


class IsAdminOrReadOnly(permissions.BasePermission):
    """Доступ Администратор или только просмотр."""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user.is_authenticated
                and (request.user.access_administrator
                     or request.user.is_superuser))
        )
