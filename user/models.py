from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    photo = models.ImageField(upload_to="avatars", blank=True, null=True)
    bio = models.CharField(max_length=600, blank=True, null=True)

class Subscribe(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscribing")
    subscribing = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscriber")
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="send_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receive_messagges")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    content = models.TextField()