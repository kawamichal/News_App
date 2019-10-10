from django.urls import path

from posts.views import BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='home')
]