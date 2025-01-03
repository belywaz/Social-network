from django.urls import path
from .views import *
from social_network.urls import *

urlpatterns = [
    path("user", UserListView.as_view(), name="user-list"),
    path("subscribe", SubscribeListView.as_view(), name="subscribe-list"),
    path("message", MessageListView.as_view(), name="message-list"),
    path("user-account/<int:pk>", UserAccountListView.as_view(), name="user-account"),
    path("user-delete/<int:pk>", UserDeleteView.as_view(), name="user-delete"),
    path("user-update/<int:pk>", UserUpdateView.as_view(), name="user-update"),
]