from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from typing import Any, Dict
from comments.models import CommentModel
from comments.forms import CommentForm
from blogs.models import BlogsModel
from accounts.models import UserProfile

class CommentView(CreateView):
    model = CommentModel
    form_class = CommentForm
    template_name = "comments/comment.html"

    def get_success_url(self) -> str:
        self.success_url = reverse_lazy("detail", kwargs={"pk": self.kwargs.get("post_id")})
        return self.success_url

    def get_queryset(self):
        blog_id = self.kwargs.get("post_id")
        object = get_object_or_404(klass=BlogsModel, id=blog_id)
        return object
    
    def get_user_object(self):
        user_id = self.request.user.id
        user = get_object_or_404(UserProfile, id=user_id)
        return user

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({"post_id": self.kwargs.get("post_id")})
        return context

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.form_class(data=request.POST)
        if form.is_valid():
            if not request.user.is_authenticated:
                return HttpResponseRedirect(reverse_lazy("login"))
            comment = form.cleaned_data.get("comment")
            print("form being valid")
            model = CommentModel(
                blog_id=self.get_queryset(), user=self.get_user_object(), comment=comment)
            model.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponse("Form is invalid")
        
class DeleteComment(DeleteView):
    model = CommentModel
    template_name = "comments/commentmodel_confirm_delete.html"
    pk_url_kwarg = "pk"

    def get_success_url(self) -> str:
        self.success_url = reverse_lazy("detail", kwargs={"pk": self.kwargs.get("pk")})
        return self.success_url

def profile(request):
    if request.user.is_authenticated:
        return render(request, "dashboard/profile.html", {"request": request})
    else:
        return HttpResponseRedirect(reverse_lazy("login"))
