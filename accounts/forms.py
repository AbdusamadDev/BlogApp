from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from accounts.models import UserProfile


class UserProfileCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = [
            "username", "email", "avatar", "birthdate", "gender", "bio", "password1", "password2"
            ]

        widgets = {
            "password1": forms.PasswordInput(),
            "birthdate": forms.DateTimeInput(),
            "bio": forms.Textarea()
        }

class UserLoginForm(AuthenticationForm):
    class Meta:
        fields = ["username", "password"]

        widgets = {
            "password": forms.PasswordInput()
        }
