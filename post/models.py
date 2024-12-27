from django.db import models
from user.models import User

# Create your models here.
class Post(models.Model):
    photo = models.ImageField(upload_to="avatars", blank=True, null=True)
    content = models.CharField(max_length=25, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creating")

    def __str__(self):
        return self.content

class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liking")
    liking = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liker")

class Coment(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="send_coment")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receive_ccoment")
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()