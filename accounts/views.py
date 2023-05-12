from django.urls import reverse_lazy
from django.views.generic import FormView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView

from accounts.models import UserProfile
from accounts.forms import UserProfileCreationForm, UserLoginForm


class Registration(FormView):
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")
    form_class = UserProfileCreationForm
    model = UserProfile

    def post(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            gender = form.cleaned_data.get("gender")
            birthdate = form.cleaned_data.get("birthdate")
            avatar = form.cleaned_data.get("avatar")
            bio = form.cleaned_data.get("bio")
            self.model.objects.create_user(
                username=username,
                email=email,
                password=password,
                bio=bio,
                avatar=avatar,
                birthdate=birthdate,
                gender=gender
            )
            return HttpResponseRedirect(self.success_url)
        else:
            return HttpResponse(str(form.errors))


class Login(LoginView):
    template_name = "registration/login.html"
    success_url = reverse_lazy("list")
    form_class = UserLoginForm
