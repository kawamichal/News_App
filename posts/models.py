from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )

    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # !add related_name later!
    text = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='publish_date') # converts the obtained data (eg. title) into URL with hyphens instead of spaces
    publish_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=CHOICES, default=DRAFT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
