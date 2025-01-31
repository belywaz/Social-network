from dataclasses import field
from django import forms
from .models import Post, Coment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["photo", "content"]

class ComentForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ["content"]

class LikeForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ["creater"]