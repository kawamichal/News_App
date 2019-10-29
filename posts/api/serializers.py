from rest_framework import serializers
from taggit.models import Tag

from posts.models import Post

from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'text', 'category', 'publish_date', 'slug', 'tags']
