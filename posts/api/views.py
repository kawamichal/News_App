from rest_framework import generics

from posts.api.serializers import PostSerializer
from posts.models import Post


class PostList(generics.ListAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

