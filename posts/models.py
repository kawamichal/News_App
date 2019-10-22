from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

DRAFT = 'draft'
PUBLISHED = 'published'
CHOICES = (
    (DRAFT, 'Draft'),
    (PUBLISHED, 'Published')
)


# menager that filters only published posts
# https://docs.djangoproject.com/en/2.2/topics/db/managers/#modifying-a-manager-s-initial-queryset
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=PUBLISHED)


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # !add related_name later!
    text = models.TextField()
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish_date')  # converts the obtained data (eg. title) into URL with hyphens instead of spaces
    publish_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=CHOICES, default=DRAFT)

    objects = models.Manager()  # default manager for all posts
    published = PublishedManager()  # custom manager only for published posts

    def __str__(self):
        return self.title

    # default ordering of the posts according to the publish date
    class Meta:
        ordering = ('-publish_date',)
