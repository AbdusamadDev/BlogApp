from django.urls import path
from dashboard.views import MyProfileDetails, MyBlogs

urlpatterns = [
    path("<int:pk>/details/", MyProfileDetails.as_view(), name="details"),
    path("my-blogs/", MyBlogs.as_view(), name="my-blogs"),
]
