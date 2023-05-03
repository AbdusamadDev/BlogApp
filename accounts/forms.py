from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from accounts.models import UserProfile


class UserProfileCreationForm(UserCreationForm):
    """All fields in User creation process: username, 
    email, password, birthdate, bio, avatar, gender"""
    class Meta:
        model = UserProfile
        fields = [
            "username", "email", "avatar", "birthdate", "gender", "bio", "password1", "password2"
            ]

        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your Email here"
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your Username here"
                }
            ),
            "birthdate": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                    "id": "time"
                }
            ),
            "gender": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "avatar": forms.FileInput(
                attrs={
                    "class": "form-control",
                    "type": "file"
                }
            ),
            "bio": forms.Textarea(
                attrs={
                    "placeholder": "Tell us about yourself",
                    "class": "form-control"
                }
            )
        }

class UserLoginForm(AuthenticationForm):
    class Meta:
        fields = ["username", "password"]
        model = UserProfile

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "You username here",
                    "style": "margin-left: 50px"
                }
            )
        }
