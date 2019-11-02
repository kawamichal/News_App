from rest_framework import serializers

from posts.models import Post, Comment

from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'publish_date']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'publish_date']


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'category', 'text', 'publish_date', 'slug', 'tags', 'comments']
