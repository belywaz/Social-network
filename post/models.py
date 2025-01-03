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
    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liking")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")

class Coment(models.Model):
    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name="send_coment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_coments")
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.content} ({self.id})"