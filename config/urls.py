from django.contrib import admin
from django.urls import path, include
from blogs.views import BlogsListView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", BlogsListView.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path("blogs/", include("blogs.urls")),
    path("accounts/", include("accounts.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("comments/", include("comments.urls")),
    # path("ckeditor/", include("ckeditor.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
