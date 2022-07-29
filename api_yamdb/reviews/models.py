from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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