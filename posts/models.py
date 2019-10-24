from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

from taggit.managers import TaggableManager

# constant arguments for choices
from tinymce.models import HTMLField

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
    text = HTMLField()
    category = models.TextField(max_length=100)

    slug = models.SlugField(max_length=250,
                            unique_for_date='publish_date')  # converts the obtained data (eg. title) into URL with hyphens instead of spaces
    publish_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=CHOICES, default=PUBLISHED)

    # managers
    objects = models.Manager()  # default manager for all posts
    published = PublishedManager()  # custom manager only for published posts

    ordering = ['publish_date']

    tags = TaggableManager()  # taggit manager

    def __str__(self):
        return self.title

    class Meta:  # default ordering of the posts according to the publish date
        ordering = ('-publish_date',)

    def get_absolute_url(self):  # redirects to the url with edited slug
        return reverse('posts:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # update slug when post is edited
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment added to {self.post} by {self.author} on {self.publish_date}'
