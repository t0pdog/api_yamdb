from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet)
from users.views import CreateTokenView, CreateUsersView

app_name = 'api'

router = DefaultRouter()
router.register('titles', TitleViewSet, basename='titles')
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
                r'/comments', CommentViewSet, basename='comments')

auth_patterns = ([
    path(
        'signup/',
        CreateUsersView.as_view(),
        name='user_signup'
    ),
    path(
        'token/',
        CreateTokenView.as_view(),
        name='token_obtain_pair'
    ),
])

urlpatterns = [
    path('v1/auth/', include(auth_patterns)),
    path('v1/users/', include('users.urls')),
    path('v1/', include(router.urls)),
]
