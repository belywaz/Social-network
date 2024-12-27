from django.urls import path
from .views import *
from social_network.urls import *

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("like", LikeListView.as_view(), name="like-list"),
    path("coment", ComentListView.as_view(), name="coment-list"),
    path("post-detail/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("post-delete/<int:pk>", PostDeleteView.as_view(), name="post-delete"),
    path("post-update/<int:pk>", PostUpdateView.as_view(), name="post-update"),
    path("post-create", PostCreateView.as_view(), name="post-create"),
]