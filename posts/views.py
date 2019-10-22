# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from posts.models import Post


class BlogListView(ListView):
    queryset = Post.published.all() # modifies the displayed posts to only those with status = published
    model = Post
    template_name = 'posts/home.html'
    paginate_by = 2 #how many posts will be displayed


class BlogDetailView(DetailView):
    queryset = Post.published.all()
    model = Post
    template_name = 'posts/detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'posts/new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'posts/update.html'
    fields = ['title', 'text']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('home')
