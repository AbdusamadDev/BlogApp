from django import forms

from comments.models import CommentModel

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ["comment"]
