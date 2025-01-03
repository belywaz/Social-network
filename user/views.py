from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import UserIsOwnerMixin
from django.urls import reverse_lazy, reverse
from .forms import *

# Create your views here.
class UserListView(ListView):
    model = User
    template_name = "user/index.html"
    context_object_name = "user"


class SubscribeListView(ListView):
    model = Subscribe
    template_name = "user/index.html"
    context_object_name = "subscribe"


class MessageListView(ListView):
    model = Message
    template_name = "user/index.html"
    context_object_name = "message"


class UserAccountListView(DetailView):
    model = User
    template_name = "user/user_account.html"
    context_object_name = "user"

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