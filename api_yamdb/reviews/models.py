from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
import datetime

ROLE_CHOICES = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Администратор'),
)


class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Пользовательские роли',
        max_length=16,
        choices=ROLE_CHOICES,
        default='user',
    )


class Review(models.Model):
    title = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE,   
    )
    text = models.TextField(),
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
        related_name = 'comments',
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
    year = models.IntegerField(max_value=datetime.now().year)
    rating = models.IntegerField(null=True, default=None)
    description = models.TextField(blank=True, null=True)
    genre = models.ManyToManyField(
        'Genre',
        null=True,
        on_delete=models.SET_NULL,
        related_name="titles",
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
