from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import AdminUsersViewSet, AdminUserViewSet

app_name = 'users'

router = DefaultRouter()
router.register('', AdminUsersViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path(
        '<str:username>/',
        AdminUserViewSet.as_view(
            {'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}
        ),
        name='usersname'
    ),
]
