from django.urls import path

from posts.api.views import PostList

urlpatterns = [
    path('posts/', PostList.as_view()),
]