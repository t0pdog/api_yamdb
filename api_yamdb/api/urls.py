from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import (AdminUsersViewSet, AdminUserViewSet, CreateTokenView,
                         CreateUsersView, MeUserViewSet)

from .views import CategoryViewSet, GenreViewSet, TitleViewSet

app_name = 'api'

router = DefaultRouter()
router.register('titles', TitleViewSet, basename='titles')
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register('users', AdminUsersViewSet, basename='users')

urlpatterns = [
    path(
        'v1/auth/signup/',
        CreateUsersView.as_view(),
        name='user_signup'
    ),
    path(
        'v1/users/me/',
        MeUserViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update'}),
        name='me'
    ),
    path(
        'v1/users/<str:username>/',
        AdminUserViewSet.as_view(
            {'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}
        ),
        name='usersname'
    ),
    path(
        'v1/auth/token/',
        CreateTokenView.as_view(),
        name='token_obtain_pair'
    ),
    path('v1/', include(router.urls)),
]
