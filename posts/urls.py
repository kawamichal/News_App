from django.urls import path

from posts.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = 'posts'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('<slug>', BlogDetailView.as_view(), name="detail"),
    path('post/new', BlogCreateView.as_view(), name='new'),
    path('<slug>/update', BlogUpdateView.as_view(), name='update'),
    path('<slug>/delete', BlogDeleteView.as_view(), name='delete')
]