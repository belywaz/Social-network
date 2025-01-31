from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy, reverse
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import PostIsOwnerMixin, ComentIsOwnerMixin
from .forms import *
from django.http import HttpResponseRedirect
from user.models import *

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "post/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        posts = Post.objects.filter(
            creater__in=Subscribe.objects.filter(
                subscribing=self.request.user
            ).values_list('subscriber', flat=True))
            
        for post in posts:
            post.is_liked = post.is_user_likes(self.request.user)

        return posts


class LikeListView(ListView):
    model = Like
    template_name = "post/post_list.html"
    context_object_name = "like"


class ComentListView(ListView):
    model = Coment
    template_name = "index.html"
    context_object_name = "coment"


class PostAllView(ListView):
    model = Post
    template_name = "post/post_all.html"
    context_object_name = "posts"

    def get_queryset(self):
        posts = Post.objects.all()
        for post in posts:
            post.is_liked = post.is_user_likes(self.request.user)

        return posts


class PostDetailView(DetailView):
    model = Post
    template_name = "post/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_liked"] = self.get_object().is_user_likes(self.request.user)
        return context


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
    fields = ["photo", "content"]


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post/post_create.html"
    form_class = PostForm
    success_url = reverse_lazy("post-list")

    def form_valid(self, form):
        form.instance.creater = self.request.user
        form.save()
        return super().form_valid(form)
    

class ComentCreateView(LoginRequiredMixin, CreateView):
    model = Coment
    template_name = "post/post_coment.html"
    form_class = ComentForm
    
    def get_success_url(self):
        return reverse_lazy("post-detail", kwargs={"pk":self.object.post.pk})

    def form_valid(self, form):
        form.instance.creater = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs.get("pk"))
        return super().form_valid(form)


class ComentDeleteView(LoginRequiredMixin, ComentIsOwnerMixin, DeleteView):
    model = Coment
    template_name = "post/coment_delete.html"
    context_object_name = "coment"

    def get_success_url(self):
        return reverse_lazy("post-detail", kwargs={"pk":self.object.post.pk})


class ComentUpdateView(LoginRequiredMixin, ComentIsOwnerMixin, UpdateView):
    model = Coment
    template_name = "post/coment_update.html"
    context_object_name = "coment"
    fields = ["content"]

    def get_success_url(self):
        return reverse_lazy("post-detail", kwargs={"pk":self.object.post.pk})
    

class LikeCreateView(LoginRequiredMixin, CreateView):
    model = Like
    template_name = "post/post_list.html"
    form_class = LikeForm

    def get(self, request, post_id, **kwargs):
        res = Like.objects.get_or_create(post=Post.objects.get(id=post_id), creater=request.user)
        if res[1] == False:
            res[0].delete()
        refer_url = request.META.get("HTTP_REFERER")
        
        return HttpResponseRedirect(refer_url)
    
    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         is_like = Like.objects.filter(post=self.get_object(), creater=self.request.user).exists()
         context['is_like'] = is_like
         return context