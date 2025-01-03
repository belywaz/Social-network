from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy, reverse
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import PostIsOwnerMixin
from .forms import *

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "templates/index.html"
    context_object_name = "posts"


class LikeListView(ListView):
    model = Like
    template_name = "templates/index.html"
    context_object_name = "like"


class ComentListView(ListView):
    model = Coment
    template_name = "templates/index.html"
    context_object_name = "coment"


class PostDetailView(DetailView):
    model = Post
    template_name = "post/post_detail.html"
    context_object_name = "post"


class PostDeleteView(LoginRequiredMixin, PostIsOwnerMixin, DeleteView):
    model = Post
    template_name = "post/post_delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("post-list")


class PostUpdateView(LoginRequiredMixin, PostIsOwnerMixin, UpdateView):
    model = Post
    template_name = "post/post_update.html"
    context_object_name = "post"
    success_url = reverse_lazy("post-list")
    fields = ["photo", "content", "creater"]


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post/post_create.html"
    form_class = PostForm
    success_url = reverse_lazy("post-list")

    def form_valid(self, form):
        form.instance.creater = self.request.user
        return super().form_valid(form)
    

class ComentCreateView(LoginRequiredMixin, CreateView):
    model = Coment
    template_name = "post/post_coment.html"
    form_class = ComentForm
    
    def get_success_url(self):
        return reverse_lazy("post-detail", kwargs={"pk":self.object.post.pk})

    def form_valid(self, form):
        form.instance.creater = self.request.user
        print(self.kwargs.get("pk"))
        form.instance.post = Post.objects.get(pk=self.kwargs.get("pk"))
        return super().form_valid(form)