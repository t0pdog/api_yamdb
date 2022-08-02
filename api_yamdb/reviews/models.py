from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from datetime import datetime

ROLE_CHOICES = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Администратор'),
)


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


class Review(models.Model):
    title = models.ForeignKey(
        'Title',
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='review',
    )
    score = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ]
    )
    pub_date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['pub_date']


class Comments(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True
    )


class Title(models.Model):
    name = models.TextField()
    year = models.IntegerField(
        validators=[
            MaxValueValidator(datetime.now().year)
        ])
    rating = models.IntegerField(blank=True, null=True,default=None)
    description = models.TextField(blank=True, null=True)
    genre = models.ManyToManyField(
        'Genre',
    )
    category = models.ForeignKey(
        'Category',
        null=True,
        on_delete=models.SET_NULL,
        related_name="titles",
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Произведение'

    
class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Жанр'


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
