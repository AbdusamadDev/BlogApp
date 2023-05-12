from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    DeleteView
)

from accounts.models import UserProfile
from blogs.models import BlogsModel
from blogs.forms import CreateBlogForm
from comments.models import CommentModel

from typing import Any, Dict


class DetailsView(DetailView):
    """Fetch one data from database"""

    template_name = "blogs/detail.html"
    model = BlogsModel
    queryset = BlogsModel.objects.all()
    context_object_name = "object"
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        pk = self.kwargs.get("pk")
        comments = CommentModel.objects.filter(blog_id=pk)
        if comments:
            comment = super().get_context_data(**kwargs)
            comment.update({"comments": comments})
            print(comment)
            return comment
        else:
            return super().get_context_data(**kwargs)


class CreateBlogView(LoginRequiredMixin, CreateView):
    """
    Creating blogs 
    Main logic goes here
    """
    request = HttpRequest
    login_url = "accounts/login/"
    template_name = "blogs/create.html"
    form_class = CreateBlogForm
    model = BlogsModel
    success_url = reverse_lazy("list")

    def post(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            user_id = UserProfile.objects.get(pk=request.user.id)
            title = form.cleaned_data.get("title")
            image = form.cleaned_data.get("image")
            content = form.cleaned_data.get("content")
            model = self.model(title=title, user=user_id, content=content, image=image)
            model.save()
            messages.success(request=request, message="Blog posted successfully!")
            return HttpResponseRedirect(self.success_url)
        else:
            return HttpResponse(str(form.errors))


class BlogsListView(ListView):
    """
    List all records from database using pagination
    No functions were over writen because no need to
    """

    http_method_names = ["get"]
    queryset = BlogsModel.objects.all().order_by("?")
    template_name = "home.html"
    paginate_by = 5

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        users = UserProfile.objects.all().values("username", "gender", "bio", "pk", "date_joined")
        context = super().get_context_data(**kwargs)
        context.update({"users": users})
        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # try:
        return super().get(request, *args, **kwargs)
    # except Exception:
    #     return HttpResponse("Sorry page is not available due to some internal problems")


class DeleteBlogView(DeleteView):
    """Delete Blog post which only belongs to user's itself"""

    queryset = BlogsModel.objects.all()
    model = BlogsModel
    success_url = reverse_lazy("home")

    def delete(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        username = request.user.username  # Here should be updated to id
        object = self.queryset.get(pk=kwargs.get("pk"))
        if object.user == username:
            object.delete()
        else:
            return HttpResponse("You don't have permission to delete other's blog")
        return HttpResponseRedirect(self.success_url)


def home(request):
    # try:
    context = {}
    return render(request, "home.html", context=context)
# except Exception:
#     return HttpResponse("Sorry page is not available due to some internal problems")
