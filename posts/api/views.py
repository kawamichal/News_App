from django.shortcuts import get_object_or_404
from rest_framework import generics

from posts.api.serializers import PostSerializer, PostListSerializer, CommentSerializer
from posts.models import Post, Comment


class PostList(generics.ListAPIView):
    queryset = Post.published.all()
    serializer_class = PostListSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer


class CommentByPostList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['pk'])
