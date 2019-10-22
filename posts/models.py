from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# constant arguments for choices
from taggit.managers import TaggableManager

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
    # converts the obtained data (eg. title) into URL with hyphens instead of spaces
    slug = models.SlugField(max_length=250, unique_for_date='publish_date')
    publish_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=CHOICES, default=PUBLISHED)

    # managers
    objects = models.Manager()  # default manager for all posts
    published = PublishedManager()  # custom manager only for published posts

    # taggit manager
    tags = TaggableManager()

    def __str__(self):
        return self.title

    # default ordering of the posts according to the publish date
    class Meta:
        ordering = ('-publish_date',)

    # redirects to the url with edited slug
    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'slug': self.slug})

    # update slug when post is edited
    def save(self, *args, **kwargs):
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
