from django.urls import path

from posts.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>', BlogDetailView.as_view(), name="detail"),
    path('post/new', BlogCreateView.as_view(), name='new'),
    path('post/<int:pk>/update', BlogUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='delete')
]