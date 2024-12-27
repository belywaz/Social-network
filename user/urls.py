from django.urls import path
from .views import *

urlpatterns = [
    path("user", UserListView.as_view(), name="user-list"),
    path("subscribe", SubscribeListView.as_view(), name="subscribe-list"),
    path("message", MessageListView.as_view(), name="message-list"),
    path("user-account/<int:pk>/", UaserAccountListView.as_view(), name="user-account"),
]