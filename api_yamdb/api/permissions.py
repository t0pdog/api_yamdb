from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Доступ Администратор или только просмотр."""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_authenticated:
            return (request.user.access_administrator
                    or request.user.is_superuser)
        else:
            return False


class IsOwnerOrHigherOrReadOnly(permissions.BasePermission):
    """Доступ владелец или выше, иначе только просмотр.

    Не авторизированному пользователю доступны только безопасные методы.
    Создание объекта доступно любому авторизированному пользователю.
    Изменение, удаление объекта доступно владельцу, модератору, администратору
    и суперюзеру Django.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif obj.author == request.user:
            return True
        elif request.user.access_moderator:
            return True
        return request.user.access_administrator or request.user.is_superuser
