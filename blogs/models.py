from django.db import models
from accounts.models import UserProfile

import os

class BlogsModel(models.Model):
    title = models.CharField(max_length=200, null=False, unique=False)
    content = models.TextField(max_length=7000, null=False, unique=False)
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True, default="")
    user = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return f"Query ({self.pk}) <{self.title}>"

    class Meta:
        indexes = [
            models.Index(fields=["title"], name="title_index")
        ]
    