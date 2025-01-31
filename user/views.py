from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import UserIsOwnerMixin
from django.urls import reverse_lazy, reverse
from .forms import *
from django.http import HttpResponseRedirect
from post.models import Post

# Create your views here.
class UserListView(ListView):
    model = User
    template_name = "user/index.html"
    context_object_name = "user"


class SubscriberListView(ListView):
    model = Subscribe
    template_name = "user/subscribers_list.html"
    context_object_name = "subscribers"

    def get_queryset(self):
        user = self.request.user
        queryset = Subscribe.objects.filter(subscribing=user).order_by("-created_at")

        return queryset


class MessageListView(ListView):
    model = Message
    template_name = "user/user_message.html"
    context_object_name = "messages"

    def get_queryset(self):
        user_id = int(self.kwargs.get("pk"))
        user1 = User.objects.get(id=user_id)
        user2 = self.request.user
        queryset = Message.objects.filter(sender=user1, receiver=user2).union(Message.objects.filter(sender=user2, receiver=user1))
        for message in queryset:
            message.is_own = message.sender == user2
        
        return queryset
    
    def post(self, request, *args, **kwargs):
        creater = self.request.user
        receiver = User.objects.get(id=int(self.kwargs.get("pk")))
        content = request.POST.get('content', '').strip()
        print(f"Sender: {creater}, Receiver: {receiver}, Content: '{content}'")
        if content:
            message = Message(sender=creater, receiver=receiver, content=content).save()


        return HttpResponseRedirect(self.request.path)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = int(self.kwargs.get("pk"))
        context['chat_user'] = User.objects.get(id=user_id)
        return context


class UserAccountView(DetailView):
    model = User
    template_name = "user/user_account.html"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        is_subscribed = Subscribe.objects.filter(subscriber=self.get_object(), subscribing=self.request.user).exists()
        context['is_subscribed'] = is_subscribed
        posts = Post.objects.filter(creater=self.get_object())

        for post in posts:
            post.is_liked = post.is_user_likes(self.request.user)
        context["posts"] = posts

        return context
        


class UserDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = User
    template_name = "user/user_delete.html"
    context_object_name = "user"
    success_url = reverse_lazy("post-list")


class UserUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = User
    template_name = "user/user_update.html"
    context_object_name = "user"
    fields = ["password", "username", "first_name", "last_name", "photo", "bio"]

    def get_success_url(self):
        return reverse_lazy("user-account", kwargs={"pk":self.object.pk})


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    template_name = "user_create.html"
    form_class = UserForm
    success_url = reverse_lazy("user-account")

    def form_valid(self, form):
        form.instance.creater = self.request.user
        return super().form_valid(form)
    

class SubscribeCreateView(LoginRequiredMixin, CreateView):
    model = Subscribe
    template_name = "user/user_account.html"
    form_class = SubscribeForm

    def get(self, request, pk, **kwargs):
        res = Subscribe.objects.get_or_create(subscriber=User.objects.get(id=pk), subscribing=request.user)
        if res[1] == False:
            res[0].delete()
        refer_url = request.META.get("HTTP_REFERER")

        return HttpResponseRedirect(refer_url)
    

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    template_name = "user/user_account.html"
    form_class = MessageForm

    def get(self, request, pk, **kwargs):
        res = Message.objects.get_or_create(sender=User.objects.get(id=pk), receiver=request.user)
        if res[1] == False:
            res[0].delete()
        refer_url = request.META.get("HTTP_REFERER")

        # return HttpResponseRedirect(refer_url)
    
    def post(self, request, pk, **kwargs):
        print("post")

        return HttpResponseRedirect("/")
    
    def form_valid(self):
        print("pintr")