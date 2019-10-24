# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from taggit.models import Tag

from posts.forms import CommentForm
from posts.models import Post


# class based views
class BlogListView(ListView):
    queryset = Post.published.all()  # modifies the displayed posts to only those with status = published
    model = Post
    template_name = 'posts/home.html'
    paginate_by = 5  # how many posts will be displayed


class BlogDetailView(DetailView):
    queryset = Post.published.all()
    model = Post
    template_name = 'posts/detail.html'


# Function based views
def comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('posts:detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'posts/comment.html', {'form': form})


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags__in=[tag])

    context = {
        'tag': tag,
        'posts': posts,
    }
    return render(request, 'posts/tag_list.html', context)

# legacy views
# class BlogCreateView(CreateView):
#     model = Post
#     template_name = 'posts/new_legacy.html'
#     fields = ['title', 'author', 'text', 'tags']
#     success_url = reverse_lazy('posts:home')
#
#
# class BlogUpdateView(UpdateView):
#     model = Post
#     template_name = 'posts/update_legacy.html'
#     fields = ['title', 'text']
#
#
# class BlogDeleteView(DeleteView):
#     model = Post
#     template_name = 'posts/delete_legacy.html'
#     success_url = reverse_lazy('posts:home')
