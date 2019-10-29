from django.urls import path

from posts.api.views import PostList, PostDetail, CommentList

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('posts/comments/', CommentList.as_view())
]