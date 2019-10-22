from django.urls import path

from posts import views
from posts.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = 'posts'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('<slug>', BlogDetailView.as_view(), name="detail"),
    path('<slug>/comment', views.comment, name="comment"),
    path('post/new', BlogCreateView.as_view(), name='new'),
    path('<slug>/update', BlogUpdateView.as_view(), name='update'),
    path('<slug>/delete', BlogDeleteView.as_view(), name='delete'),
    path('topic/<slug:slug>/', views.tagged, name='tagged')
]