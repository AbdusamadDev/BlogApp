from django.db import models

from accounts.models import UserProfile
from blogs.models import BlogsModel

class CommentModel(models.Model):
    blog_id = models.ForeignKey(to=BlogsModel, on_delete=models.CASCADE)
    user = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)
    comment = models.TextField(max_length=4000, unique=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "Query <{}> Content: <{}>".format(self.blog_id, self.comment)
    
    class Meta:
        indexes = [
            models.Index(fields=["blog_id"], name="blog_id_index")
        ]
