from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User


class Title(models.Model):
    name = models.TextField(verbose_name='название')
    year = models.IntegerField(verbose_name='Дата выхода')
    rating = models.IntegerField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Рейтинг'
    )
    description = models.TextField(blank=True, verbose_name='Описание')
    genre = models.ManyToManyField(
        'Genre',
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        'Category',
        verbose_name='Категория',
        null=True,
        on_delete=models.SET_NULL,
        related_name="titles"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Произведение'


class Genre(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    slug = models.SlugField(unique=True, verbose_name='Идентификатор')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Жанр'


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    slug = models.SlugField(unique=True, verbose_name='Идентификатор')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
       
       
class Review(models.Model):
    title = models.ForeignKey(
        'Title',
        on_delete=models.CASCADE,
        related_name='reviews'
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
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_review'
            ),
        ]


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
