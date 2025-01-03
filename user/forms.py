from dataclasses import field
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["password", "username", "first_name", "last_name", "photo", "bio"]