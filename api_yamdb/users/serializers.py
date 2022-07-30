from rest_framework import serializers

from reviews.models import User


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'confirmation_code')
