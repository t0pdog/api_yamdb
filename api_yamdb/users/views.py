from django.core.mail import send_mail
from rest_framework import status, serializers
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.tokens import default_token_generator

from .serializers import CreateUserSerializer
from reviews.models import User


class CreateUsersView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user, created = User.objects.get_or_create(
                email=serializer.validated_data['email'],
                username=serializer.validated_data['username'],
            )
            confirmation_code = default_token_generator.make_token(user)
            send_mail(
                'Код подтверждения',
                f'Код подтверждения: {confirmation_code}',
                'from@example.com',
                [user.email]
            )
            return Response(serializer.validated_data,
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateTokenView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        confirmation_code = request.data['confirmation_code']
        user = get_object_or_404(User, username=request.data['username'])
        if confirmation_code != user.confirmation_code:
            raise serializers.ValidationError(
                'Вы используете не верный код подтверждения!')
        refresh = RefreshToken.for_user(user)
        return Response({'token': str(refresh.access_token)},
                        status=status.HTTP_200_OK)
