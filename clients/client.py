# I will give you all apps code which includes authentication, commenting, blog_posting, and dashboard apps

# First, blogs app
# Here is my views.py in blogsapp:

# from django.shortcuts import render
# from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
# from django.urls import reverse_lazy
# from django.contrib import messages
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import (
#     CreateView, 
#     DetailView, 
#     ListView,
#     DeleteView
# )

# from accounts.models import UserProfile
# from blogs.models import BlogsModel
# from blogs.forms import CreateBlogForm
# from comments.models import CommentModel

# from typing import Any, Dict
# from PIL import Image


# class DetailsView(DetailView):
#     """Fetch one data from database"""

#     template_name = "blogs/detail.html"
#     model = BlogsModel
#     queryset = BlogsModel.objects.all()
#     context_object_name = "object"
#     pk_url_kwarg = "pk"

#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         pk = self.kwargs.get("pk")
#         comments = CommentModel.objects.filter(blog_id=pk)
#         if comments:
#             comment = super().get_context_data(**kwargs)
#             comment.update({"comments": comments})
#             print(comment)
#             return comment
#         else:
#             return super().get_context_data(**kwargs)

# class CreateBlogView(LoginRequiredMixin, CreateView):
#     """
#     Creating blogs 
#     Main logic goes here
#     """
#     request = HttpRequest
#     login_url = "accounts/login/"
#     template_name = "blogs/create.html"
#     form_class = CreateBlogForm
#     login_url = "login"
#     model = BlogsModel
#     success_url = reverse_lazy("list")

#     def post(self, request: HttpRequest, *args, **kwargs):
#         try:
#             form = self.form_class(data=request.POST, files=request.FILES)
#             if form.is_valid():
#                 user_id = UserProfile.objects.get(pk=request.user.id)
#                 title   = form.cleaned_data.get("title")
#                 image   = form.cleaned_data.get("image")
#                 content = form.cleaned_data.get("content")
#                 model   = self.model(title=title, user=user_id, content=content, image=image)
#                 model.save()
#                 messages.success(request=request, message=("Blog posted successfully!"))
#                 return HttpResponseRedirect(self.success_url)
#             else:
#                 return HttpResponse(str(form.errors))
#         except Exception:
#             return HttpResponse("Sorry page is not avaliable due to some internal problems")

# class BlogsListView(ListView):
#     """
#     List all records from database using pagination
#     No functions were overriden because no need to
#     """

#     http_method_names = ["get"]
#     queryset = BlogsModel.objects.all().order_by("?")
#     template_name = "home.html"
#     paginate_by = 5

#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         users = UserProfile.objects.all().values("username", "gender", "bio", "pk", "date_joined")
#         context = super().get_context_data(**kwargs)
#         context.update({"users": users})
#         return context

#     def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
#         # try:
#             return super().get(request, *args, **kwargs)
#         # except Exception:
#         #     return HttpResponse("Sorry page is not avaliable due to some internal problems")

# class DeleteBlogView(DeleteView):
#     """Delete Blog post which only belongs to user's itself"""

#     queryset = BlogsModel.objects.all()
#     model = BlogsModel
#     success_url = reverse_lazy("home")

#     def delete(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
#         try:
#             username = request.user.username # Here should be updated to id
#             object = self.queryset.get(pk=kwargs.get("pk"))
#             if object.user == username:
#                 object.delete()
#             else:
#                 return HttpResponse("You don't have permission to delete other's blog")
#             return HttpResponseRedirect(self.success_url)
#         except Exception:
#             return HttpResponse("Sorry page is not avaliable due to some internal problems")
    
# def home(request):
#     # try:
#         context = {}
#         return render(request, "home.html", context=context)
#     # except Exception:
#     #     return HttpResponse("Sorry page is not avaliable due to some internal problems")

# here is my urls.py in blogs app:

# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static

# from blogs import views

# urlpatterns = [
#     path("create/", view=views.CreateBlogView.as_view(), name="create"),
#     path("detail/<int:pk>/", view=views.DetailsView.as_view(), name="detail"),
#     path("list/", views.BlogsListView.as_view(), name="list"),
#     path("delete/<int:pk>/", views.DeleteBlogView.as_view(), name="delete")
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# here is my models.py in blogs app:

# from django.db import models
# from accounts.models import UserProfile


# from ckeditor.fields import RichTextField
# import os

# class BlogsModel(models.Model):
#     title = models.CharField(max_length=200, null=False, unique=False)
#     content = RichTextField(max_length=7000, null=False, unique=False)
#     image = models.ImageField(upload_to="blog_images/", blank=True, null=True, default="")
#     user = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True, blank=True)

#     def __str__(self) -> str:
#         return f"Query ({self.pk}) <{self.title}>"

#     class Meta:
#         indexes = [
#             models.Index(fields=["title"], name="title_index")
#         ]
    
# here is my forms.py in blogs app:

# from django import forms
# from blogs.models import BlogsModel


# class CreateBlogForm(forms.ModelForm):
#     class Meta:
#         model = BlogsModel
#         fields = ["title", "content", "image"]

#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.fields['image'].required = False

# class UpdateBlogForm(forms.ModelForm):
#     class Meta:
#         model = BlogsModel
#         fields = ["title", "content", "image"]
 
#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.fields['image'].required = False

# so, this was blogs app source code now lets turn to dashboard app
# here is views.py in my dashboard app:

# from django.shortcuts import render
# from django.views.generic import DetailView, ListView
# from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
# from django.urls import reverse_lazy

# from accounts.models import UserProfile
# from blogs.models import BlogsModel

# class MyProfileDetails(DetailView):
#     template_name = "dashboard/my_profile.html"
#     model = UserProfile
#     pk_url_kwarg = "pk"

#     def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
#         try:
#             return super().get(request, *args, **kwargs)
#         except Exception:
#             return HttpResponse("Sorry page is not avaliable due to some internal problems")

# class MyBlogs(ListView):
#     template_name = "dashboard/my_blogs.html"
#     model = BlogsModel
#     pk_url_kwarg = "pk"
#     context_object_name = "object"
#     paginate_by = 20

#     def get_queryset(self):
#         if self.request.user.is_authenticated:
#             pk = self.request.user.id
#         else:
#             return HttpResponseRedirect(reverse_lazy("login"))
#         model = self.model.objects.filter(user_id=pk)
#         return model
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update({"blogs": self.get_queryset()})
#         return context

#     def get(self, request: HttpRequest, *args, **kwargs):
#         try:
#             self.object_list = self.get_queryset()
#             return self.render_to_response(self.get_context_data(**kwargs))
#         except Exception:
#             return HttpResponse("Sorry page is not avaliable due to some internal problems")

# here is urls.py in dashboard app:

# from django.urls import path
# from dashboard.views import MyProfileDetails, MyBlogs

# urlpatterns = [
#     path("<int:pk>/details/", MyProfileDetails.as_view(), name="details"),
#     path("my-blogs/", MyBlogs.as_view(), name="my-blogs"),
# ]

# there is no models.py and forms.py code in dashboard cause no need to
# and now lets turn to comments app
# here is views.py in comments app:

# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import CreateView, DeleteView
# from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

# from typing import Any, Dict
# from comments.models import CommentModel
# from comments.forms import CommentForm
# from blogs.models import BlogsModel
# from accounts.models import UserProfile

# class CommentView(LoginRequiredMixin, CreateView):
#     model = CommentModel
#     login_url = "login"
#     form_class = CommentForm
#     template_name = "comments/comment.html"

#     def get_success_url(self) -> str:
#         self.success_url = reverse_lazy("detail", kwargs={"pk": self.kwargs.get("post_id")})
#         return self.success_url

#     def get_queryset(self):
#         blog_id = self.kwargs.get("post_id")
#         object = get_object_or_404(klass=BlogsModel, id=blog_id)
#         return object
    
#     def get_user_object(self):
#         user_id = self.request.user.id
#         user = get_object_or_404(UserProfile, id=user_id)
#         return user

#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context.update({"post_id": self.kwargs.get("post_id")})
#         return context

#     def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
#         # if not request.user.is_authenticated:
#         #     print("not authenticated 0000")
#         #     return HttpResponseRedirect(reverse_lazy("login"))
#         form = self.form_class(data=request.POST)
#         if form.is_valid():
#             print("Not Authenticated 000")
#             comment = form.cleaned_data.get("comment")
#             print("form being valid")
#             model = CommentModel(
#                 blog_id=self.get_queryset(), user=self.get_user_object(), comment=comment)
#             model.save()
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return HttpResponse("Form is invalid")
            

# class DeleteComment(DeleteView):
#     model = CommentModel
#     template_name = "comments/commentmodel_confirm_delete.html"
#     pk_url_kwarg = "pk"

#     def get_success_url(self) -> str:
#         self.success_url = reverse_lazy("detail", kwargs={"pk": self.kwargs.get("pk")})
#         return self.success_url
    
#     def delete(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
#         if not request.user.is_authenticated:
#             return HttpResponseRedirect(reverse_lazy("login"))
#         return super().delete(request, *args, **kwargs)

# def profile(request):
#     if request.user.is_authenticated:
#         return render(request, "dashboard/profile.html", {"request": request})
#     else:
#         return HttpResponseRedirect(reverse_lazy("login"))

# here is my urls.py in comments app:

# from django.urls import path

# from comments.views import CommentView, DeleteComment, profile

# urlpatterns = [
#     path("comment/<int:post_id>/", CommentView.as_view(), name="comment"),
#     path("delete-comment/<int:pk>", DeleteComment.as_view(), name="delete-comment"),
#     path("profile/", profile, name="profile")
# ]

# here is forms.py in comments app:
# from django import forms

# from comments.models import CommentModel

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = CommentModel
#         fields = ["comment"]

# here is models.py file in comments app
# note that I am backend developer and am not master at frontend but have basic knowledge:
# and finally authentication app called "accounts" I have overwrote django's builtin core app - accounts
# here is views.py file in accounts app:

# from django.shortcuts import render
# from django.urls import reverse_lazy
# from django.views.generic import FormView, DetailView
# from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
# from django.contrib.auth.views import LoginView

# from accounts.models import UserProfile
# from accounts.forms import UserProfileCreationForm, UserLoginForm


# class Registration(FormView):
#     template_name = "registration/register.html"
#     success_url = reverse_lazy("login")
#     form_class = UserProfileCreationForm
#     model = UserProfile

#     def post(self, request: HttpRequest, *args, **kwargs):
#         try:
#             form = self.form_class(request.POST, request.FILES)
#             if form.is_valid():
#                 username = form.cleaned_data.get("username")
#                 email = form.cleaned_data.get("email")
#                 password = form.cleaned_data.get("password1")
#                 gender = form.cleaned_data.get("gender")
#                 birthdate = form.cleaned_data.get("birthdate")
#                 avatar = form.cleaned_data.get("avatar")
#                 bio = form.cleaned_data.get("bio")
#                 user = self.model.objects.create_user(
#                     username=username, 
#                     email=email, 
#                     password=password, 
#                     bio=bio,
#                     avatar=avatar, 
#                     birthdate=birthdate,
#                     gender=gender
#                 )
#                 return HttpResponseRedirect(self.success_url)
#             else:
#                 return HttpResponse(str(form.errors))
#         except Exception:
#             return HttpResponse("Sorry page is not avaliable due to some internal problems")

# class Login(LoginView):
#     template_name = "registration/login.html"
#     success_url = reverse_lazy("list")
#     form_class = UserLoginForm  

#     def post(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
#         try:
#             print(self.request.POST)
#             return super().post(request, *args, **kwargs)
#         except Exception:
#             return HttpResponse("Sorry page is not avaliable due to some internal problems")

# and here is urls.py in accounts app:
# from django.contrib.auth.views import LogoutView
# from django.urls import path
# from django.conf.urls.static import static
# from django.conf import settings

# from accounts import views

# urlpatterns = [
#     path("register/", views.Registration.as_view(), name="register"),
#     path("login/", views.Login.as_view(), name="login"),
#     path("logout/", LogoutView.as_view(), name="logout"),
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# here is forms.py in accounts app:

# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# from accounts.models import UserProfile


# class UserProfileCreationForm(UserCreationForm):
#     class Meta:
#         model = UserProfile
#         fields = [
#             "username", "email", "avatar", "birthdate", "gender", "bio", "password1", "password2"
#             ]

#         widgets = {
#             "password1": forms.PasswordInput(),
#             "birthdate": forms.DateTimeInput(),
#             "bio": forms.Textarea()
#         }

# class UserLoginForm(AuthenticationForm):
#     class Meta:
#         fields = ["username", "password"]

#         widgets = {
#             "password": forms.PasswordInput()
#         }
# and here is my models.py, and I have overwrote django's default User model
# here is models.py file in accounts app:
# from django.db import models
# from django.contrib.auth.models import AbstractUser, Group, Permission

# CHOICES = (
#     ("Male", "Male"),
#     ("Female", "Female")
# )

# # avatar, date_of_birth, gender, date_joined
# class UserProfile(AbstractUser):
#     bio = models.CharField(max_length=500)
#     avatar = models.ImageField(upload_to="avatars/")
#     date_joined = models.DateTimeField(auto_now_add=True)
#     gender = models.CharField(max_length=10, choices=CHOICES)
#     birthdate = models.DateTimeField()
#     groups = models.ManyToManyField(Group, related_name='user_profiles')
#     user_permissions = models.ManyToManyField(Permission, related_name='user_profiles')

#     def __str__(self) -> str:
#         return str((self.username, self.email, self.password, self.bio))
    
# # HINT: Add or change a related_name argument 
# # to the definition for 'auth.User.user_permissions' or 'accounts.UserProfile.user_permissions'.

# Now. here is all my templates and those are seperated by app:
# create.html in blogs app:
# {% extends 'home.html' %}

# {% block content %}
#     <form action="{% url 'create' %}" method="post" enctype="multipart/form-data">
#         {% csrf_token %}
#         {{ form.as_p }}
#         {{ form.media }}
#         <input type="submit"/>
#     </form>
# {% endblock %}

# and here is detail.html in blogs app
# {% extends 'home.html' %}

# {% block content %}
#     <div style="max-width: 900px; word-wrap: break-word;margin-left: 20%;">
#         {% if object.image != "" %}
#             <img class="img-fluid" src="{{ object.image.url }}" style="border-radius: 3%;border-style: ridge;">
#         {% endif %}
#         <br><br>
#         <h1>{{ object.title }}</h1>
#         <div style="word-wrap: break-word;">
#             <p class="card-text">{{ object.content|safe }}</p>  
#             <br><br>
#             <small>Posted by {{ object.user.username }} at <strong>{{ object.date }}</strong></small>
#         </div>
#     </div>
#     <!-- <a class="list-group-item list-group-item-action">
#         <h2>{{ object.title }}</h2>
#         <hr>
#         {% if object.image %}
#             <img src="{{ object.image.url }}">
#             <p><strong>{{ object.user.username }}</strong></p>
#             {% endif %}
#         <br>
#         <p>{{ object.content|safe }}</p>
#         <br>
#         <p>{{ object.date }}</p>
#         {{ object.pk }}
#         <br><hr>
#         <a href="{% url 'comment' post_id=object.pk %}">Comment Out</a>
#         <hr>
#         {% if comments %}
#             {% for comment in comments %}
#                 <div>
#                     <p>{{ comment.comment }} 
#                         {% if request.user.id == comment.user_id %} 
#                             ---<a href="{% url 'delete-comment' comment.pk %}">Delete</a></p>
#                         {% endif %}
#                     <p>
#                         <strong>Commented by {{ comment.user.username }} at {{ comment.date }}</strong>
#                     </p>
#                 </div>
#             {% endfor %}
#         {% endif %}
#     </a> -->
# {% endblock %}

# edit.html in blogs app
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Edit Blog</title>
# </head>
# <body>
#     <div>
#         <form action="{% url 'update' form.instance.pk %}" method="post" enctype="multipart/form-data">
#             {% csrf_token %}
#             {{ form.as_p }}
#             {{ form.media }}
#             <input type="submit"/>
#         </form>
#     </div>
# </body>
# </html>

# now lets turn to comments app
# comment.html in comments app:


# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Comment</title>
# </head>
# <body>
#     <form method="post" action="/comments/comment/{{ post_id }}/">
#         {% csrf_token %}
#         {{ form.as_p }}
#         <input type="submit"/>
#     </form>
# </body>
# </html>

# commentmodel_confirm_delete.html
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     <form action="" method="post">
#         {% csrf_token %}
#         Are you sure?
#         <input type="submit" value="Confirm" />
#     </form>
# </body>
# </html>

# now, lets turn to dashboard app
# my_blogs.html in dashboard app:

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     {% for obj in object %}
#         <div>
#             <h2>{{ obj.title }}</h2>
#             <br>
#             <img src="{{ obj.image.url }}">
#             <p>{{ obj.content|safe }}</p>
#             <hr>
#             <p><strong>Posted by {{ obj.user.username }} in {{ obj.date }}</strong></p>
#         </div>
#     {% endfor %}
#     <div>
#         {% if is_paginated %}
#             {% if page_obj.has_previous %}
#                 <a href="?page={{ page_obj.previous_page_number }}"><< Previos</a>
#             {% endif %}
#             {% if page_obj.has_next %}
#                 <a href="?page={{ page_obj.next_page_number }}">Next >></a>
#             {% endif %}
#         {% endif %}
#     </div>
# </body>
# </html>

# myprofile.html in dashboard app:
# {% extends 'home.html' %}

# {% block content %}
#     <h1>Hi, {{ object.username }}</h1>
#     <hr>
#     <p><strong>About Me<br><br>{{ object.bio }}</strong></p>
#     <p>Age: {{ object.birthdate }}</p>
#     <p>Gender: {{ object.gender }}</p>
#     <p>Member since {{ object.date_joined }}</p>
#     <img src="{{ object.avatar.url }}">
#     <br><br>
#     <a href="{% url 'my-blogs' %}">My Blogs</a>
# {% endblock %}

# profile.html in dashboard app:
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     <a href="{% url 'details' request.user.id %}">My Profile</a><br>
#     <a href="{% url 'my-blogs' %}">My Blog Posts</a><br>
# </body>
# </html>

# and now registration app templates
# details.html in registration app
# {% extends 'home.html' %}

# {% block content %}
#     <h1>Username: {{ object.username }}</h1>
#     <h3>Email: {{ object.email }}</h3>
#     <hr>
#     <p>About me:<br>{{ object.bio }}</p>
#     <p>Image: <img src="{{ object.avatar.url }}"></p>
# {% endblock %}

# login.html registration app:
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     <div>
#         <form action="{% url 'login' %}?next={{ request.path }}" method="post">
#             {% csrf_token %}
#             {{ form.as_p }}
#             <input type="hidden" name="next" value="{{ next }}" />
#             <button type="submit">Login</button>
#         </form>
#     </div>
# </body>
# </html>

# register.html in registration app:
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     <div>
#         <form action="{% url 'register' %}" method="post" enctype="multipart/form-data">
#             {% csrf_token %}
#             {{ form.as_p }}
#             <input type="submit">
#         </form>
#     </div>
# </body>
# </html>
# This is my  homepage:

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>HomePage</title>
#     <link rel="shortcut icon" type="image/png" sizes="16x16 32x32" href="data:image/png;base64,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"/>
#     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" 
#     integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
# </head>
# <body>
#     <nav class="navbar navbar-expand-lg navbar navbar-dark bg-dark">
#     <div class="container-fluid">
#         <a class="navbar-brand" style="color: chartreuse;font: bold;" href="{% url 'home' %}">BlogBar</a>
#         <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
#         <span class="navbar-toggler-icon"></span>
#         </button>
#         <div class="collapse navbar-collapse" id="navbarSupportedContent">
#         <ul class="navbar-nav me-auto mb-2 mb-lg-0">
#             <li class="nav-item dropdown">
#             <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
#                 Authentication
#             </a>
#             <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
#                 <li><a class="dropdown-item" href="{% url 'register' %}">Register</a></li>
#                 <li><a class="dropdown-item" href="{% url 'login' %}">Login</a></li>
#                 <li><a class="dropdown-item" href="#"></a></li>
#                 <li><hr class="dropdown-divider"></li>
#                 <li><a class="dropdown-item" href="{% url 'logout' %}">Logout</a></li>
#             </ul>
#             </li>
#             <a class="btn btn-outline-success" href="{% url 'create' %}">Create Blog Post</a>
#         </ul>
#         {% if request.user.is_authenticated %}
#             <a class="nav-link" style="color:beige;margin: 20px;" href="{% url 'details' user.pk %}">👨‍💻 {{ request.user.username }}</a>
#         {% else %}
#             <a class="nav-link" style="color:beige;margin: 20px;" href="{% url 'login' %}">Login</a>
#         {% endif %}
#         <form class="d-flex">
#             <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
#             <button class="btn btn-outline-light" type="submit">Search</button>
#         </form>
#         </div>
#     </div>
#     </nav>
#     <br>
#     <div class="container">
#         <div class="row">
#             <div class="list-group col-md-6" style="width: 400px;display: flex;">
#                 {% for user in users %}
#                     <a href="{% url 'details' user.pk %}" class="list-group-item list-group-item-action" aria-current="true">
#                         <div class="d-flex w-100 justify-content-between">
#                         <h5 class="mb-1">{{ user.username }}</h5>
#                         <small>{{ user.date_joined }}</small>
#                         </div>
#                         <p class="mb-1">{{ user.bio }}</p>
#                         <small>{{ user.gender }}</small>
#                     </a>
#                 {% endfor %}
#             </div>
#             <div style="padding-top: -80px;" class="col-md-6">
#                 {% for object in object_list %}
#                     <!-- <br> -->
#                     <div class="card" style="width: 50rem;left: 20%;margin-top: 10px;">
#                         <img src="{{ object.image.url }}" class="card-img-top" alt="">
#                         <div class="card-body">
#                         <h5 class="card-title">{{ object.title }}</h5>
#                         <p class="card-text">{{ object.content|safe }}</p>
#                         <a href="{% url 'detail' object.pk %}" class="btn btn-primary">Read More</a>
#                         </div>
#                     </div>
#                 {% endfor %}
#             </div>
#         </div>
#     </div>
#         {% if is_paginated %}
#             {% if page_obj.has_previous %}
#                 <a href="?page={{ page_obj.previous_page_number }}"><< Previos</a>
#             {% endif %}
#             {% if page_obj.has_next %}
#                 <a href="?page={{ page_obj.next_page_number }}">Next >></a>
#             {% endif %}
#         {% endif %}
#     </div>
#     <br>
#     {% if messages %}
#         {% for message in messages %}
#             {{ message }}
#         {% endfor %}
#     {% endif %}
#     {% block content %}
#     {% endblock %}
#     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" 
#     integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
# </body>
# <footer class="footer bg-dark">
#     <div class="container">
#       <span style="color: aliceblue;"><center><br><br>This web application is built for a portfolio purpose. 
#         However it can be used for production as well. <br>Click <a href="{% url 'details' 2 %}" class="btn-outline-light">here</a> to see Developer</center></span>
#         <br><br>
#     </div>
#   </footer>
# </html>

# and here is create.html:

# {% extends 'home.html' %}

# {% block content %}
#     <form action="{% url 'create' %}" method="post" enctype="multipart/form-data">
#         {% csrf_token %}
#         {{ form.as_p }}
#         {{ form.media }}
#         <input type="submit"/>
#     </form>
# {% endblock %}


# Note that these are all of my website source code however my frontend is not completed yet.
# I have used core features of django, bcrypt for password creation, pagination, and others.
