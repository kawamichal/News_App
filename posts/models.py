from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


