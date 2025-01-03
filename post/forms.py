from dataclasses import field
from django import forms
from .models import Post, Coment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["photo", "content", "creater"]

class ComentForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ["content"]