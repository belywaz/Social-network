from dataclasses import field
from django import forms
from .models import User, Subscribe, Message

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["password", "username", "first_name", "last_name", "photo", "bio"]

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ["subscriber", "subscribing"]


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["content"]