from django.urls import path

from comments.views import CommentView, DeleteComment, profile

urlpatterns = [
    path("comment/<int:post_id>/", CommentView.as_view(), name="comment"),
    path("delete-comment/<int:pk>", DeleteComment.as_view(), name="delete-comment"),
    path("profile/", profile, name="profile")
]
