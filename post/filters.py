from django import template
from .models import Like


regester = template.library()
@regester.filter
def is_user_likes(user, post):
    return Like.objects.filter(creater=user, post=post).exists()