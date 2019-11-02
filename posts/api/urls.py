from django.urls import path

from posts.api.views import PostList, PostDetail, CommentByPostList

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('posts/<int:pk>/comments/', CommentByPostList.as_view())
]
