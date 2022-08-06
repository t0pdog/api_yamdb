from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Переопределение стандартной модели User.

    Переопределены поля: email, first_name, last_name.
    Добавлены поля: bio, role, confirmation_code.
    """

    ADMINISTRATOR = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'

    ROLE_CHOICES = (
        (ADMINISTRATOR, 'admin'),
        (MODERATOR, 'moderator'),
        (USER, 'user')
    )

    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Адрес электронной почты',
    )
    first_name = models.TextField(
        max_length=150,
        verbose_name='Имя',
        blank=True,
    )
    last_name = models.TextField(
        max_length=150,
        verbose_name='Фамилия',
        blank=True,
    )
    bio = models.TextField(
        verbose_name='Биография',
        blank=True
    )
    role = models.CharField(
        choices=ROLE_CHOICES,
        default=USER,
        verbose_name='Права доступа',
        max_length=50,
    )

    class Meta:
        ordering = ['id']

    @property
    def access_moderator(self):
        return self.role == self.MODERATOR

    @property
    def access_administrator(self):
        return self.role == self.ADMINISTRATOR
