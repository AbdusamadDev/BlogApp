from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
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
from permissions.views import IsAuthenticatedMixin

from typing import Any, Dict, Optional

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

class CreateBlogView(IsAuthenticatedMixin, CreateView):
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
        try:
            form = self.form_class(data=request.POST, files=request.FILES)
            if form.is_valid():
                user_id = UserProfile.objects.get(pk=request.user.id)
                title   = form.cleaned_data.get("title")
                image   = form.cleaned_data.get("image")
                content = form.cleaned_data.get("content")
                print(image)
                model   = self.model(title=title, user=user_id, content=content, image=image)
                model.save()
                messages.success(request=request, message=("Blog posted successfully!"))
                return HttpResponseRedirect(self.success_url)
            else:
                return HttpResponse(str(form.errors))
        except Exception:
            return HttpResponse("Sorry page is not avaliable due to some internal problems")

class BlogsListView(ListView):
    """
    List all records from database using pagination
    No functions were overriden because no need to
    """

    http_method_names = ["get"]
    queryset = BlogsModel.objects.all().order_by("?")
    template_name = "blogs/list.html"
    paginate_by = 20 if queryset.count() > 30 else 1

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        try:
            return super().get(request, *args, **kwargs)
        except Exception:
            return HttpResponse("Sorry page is not avaliable due to some internal problems")

class DeleteBlogView(DeleteView):
    """Delete Blog post which only belongs to user's itself"""

    queryset = BlogsModel.objects.all()
    model = BlogsModel
    success_url = reverse_lazy("home")

    def delete(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        try:
            username = request.user.username # Here should be updated to id
            object = self.queryset.get(pk=kwargs.get("pk"))
            if object.user == username:
                object.delete()
            else:
                return HttpResponse("You don't have permission to delete other's blog")
            return HttpResponseRedirect(self.success_url)
        except Exception:
            return HttpResponse("Sorry page is not avaliable due to some internal problems")
    
def home(request):
    # try:
        context = {}
        return render(request, "home.html", context=context)
    # except Exception:
    #     return HttpResponse("Sorry page is not avaliable due to some internal problems")
# qweqweqwesafra
# qweqweqweqwe