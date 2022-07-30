from django.core.mail import send_mail
from rest_framework import status, serializers
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


from .serializers import CreateUserSerializer
from reviews.models import User


class CreateUsersView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        if User.objects.get(username=request.data['username']):
            user = User.objects.get(
                username=request.data['username'])
        else:
            serializer = CreateUserSerializer(data=request.data)
            if serializer.is_valid():
                user = User.objects.create_user(
                    email=serializer.validated_data['email'],
                    username=serializer.validated_data['username'],
                )
            else:
                return Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        confirmation_code = RefreshToken.for_user(user)
        send_mail(
            'Код подтверждения',
            f'Код подтверждения: {confirmation_code}',
            'from@example.com',
            [request.data['email']]
        )
        user.confirmation_code = confirmation_code
        user.save()
        return Response(request.data, status=status.HTTP_200_OK)


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
