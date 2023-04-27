from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from accounts import views

urlpatterns = [
    path("register/", views.Registration.as_view(), name="register"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

