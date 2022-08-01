from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TitleViewSet, GenreViewSet, CategoryViewSet
from .views import CommentViewSet, ReviewViewSet
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
urlpatterns = [
    path('v1/', include(router.urls)),
    path(
        'v1/auth/signup/',
        CreateUsersView.as_view(),
        name='user_signup'
    ),
    path(
        'v1/auth/token/',
        CreateTokenView.as_view(),
        name='token_obtain_pair'
    ),
]
