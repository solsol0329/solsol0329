from django.db import models
from django.conf import settings



class Movie(models.Model):

    GENRE_CHOICES = {
        ('Comedy','Comedy'),
        ('Fantasy','Fantasy'),
        ('Romance','Romance'),
    }
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    genre = models.CharField(max_length=50, choices = GENRE_CHOICES, null=True)
    score = models.FloatField(default=0, null=True)
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)