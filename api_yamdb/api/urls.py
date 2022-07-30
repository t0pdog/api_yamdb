from django.urls import include, path
from rest_framework import routers

from users.views import CreateTokenView, CreateUsersView

app_name = 'api'

router = routers.DefaultRouter()

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
