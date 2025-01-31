from django.urls import path
from .views import *
from social_network.urls import *

urlpatterns = [
    path("user", UserListView.as_view(), name="user-list"),
    path("subscribers", SubscriberListView.as_view(), name="subscribers-list"),
    path("message/<int:pk>", MessageListView.as_view(), name="message-list"),
    path("user-account/<int:pk>", UserAccountView.as_view(), name="user-account"),
    path("user-delete/<int:pk>", UserDeleteView.as_view(), name="user-delete"),
    path("user-update/<int:pk>", UserUpdateView.as_view(), name="user-update"),
    path("subscribe-user/<int:pk>", SubscribeCreateView.as_view(), name="subscribe-user"),
    path("message-create/<int:pk>", MessageCreateView.as_view(), name="message-create"),
]