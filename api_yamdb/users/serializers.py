from rest_framework import serializers

from reviews.models import User


class CreateUser:

    def __init__(self, email, username):
        self.email = email
        self.username = username


class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=256,
    )
    username = serializers.CharField(max_length=150)

    def validate(self, data):
        if data['username'] == 'me':
            raise serializers.ValidationError(
                'Вы не можете создать пользователя с таким именем!')
        is_username = User.objects.filter(
            username=data['username']).exists()
        is_email = User.objects.filter(
            email=data['email']).exists()
        if is_username is False and is_email is True:
            raise serializers.ValidationError(
                'Пользователь с таким адрес электронной почты уже'
                ' существует!'
            )
        if is_username is True and is_email is False:
            raise serializers.ValidationError(
                'Пользователь с таким именем уже существует!')
        return data


class TokenUser:

    def __init__(self, username, confirmation_code):
        self.username = username
        self.confirmation_code = confirmation_code


class TokenUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    confirmation_code = serializers.CharField(max_length=256)

    def validate(self, data):
        if data['confirmation_code'] == '':
            raise serializers.ValidationError(
                'Вы не предостваили код подтверждения!')
        return data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
        read_only_fields = ('role',)

    def update(self, instance, validated_data):
        User.objects.filter(username=instance.username).update(
            **validated_data)
        user = User.objects.get(username=instance.username)
        return user


class AdminUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
