from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blogs import views

urlpatterns = [
    path("create/", view=views.CreateBlogView.as_view(), name="create"),
    path("detail/<int:pk>/", view=views.DetailsView.as_view(), name="detail"),
    path("list/", views.BlogsListView.as_view(), name="list"),
    path("delete/<int:pk>/", views.DeleteBlogView.as_view(), name="delete")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
