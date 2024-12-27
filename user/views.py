from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

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

class UaserAccountListView(DetailView):
    model = User
    template_name = "user/user_account.html"
    context_object_name = "user"