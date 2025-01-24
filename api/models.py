from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    genres = models.CharField(max_length=255)
    platforms = models.JSONField()
    prices = models.JSONField()
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title
