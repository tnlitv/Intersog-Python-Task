from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Post, Comment


class PostList(ListView):
    queryset = Post.objects.order_by('-created_at')
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
