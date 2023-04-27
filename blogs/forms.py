from django import forms
from blogs.models import BlogsModel


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = BlogsModel
        fields = ["title", "content", "image"]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['image'].required = False

class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = BlogsModel
        fields = ["title", "content", "image"]
 
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['image'].required = False
