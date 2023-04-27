from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from accounts.models import UserProfile
from blogs.models import BlogsModel

class MyProfileDetails(DetailView):
    template_name = "dashboard/my_profile.html"
    model = UserProfile
    pk_url_kwarg = "pk"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        try:
            return super().get(request, *args, **kwargs)
        except Exception:
            return HttpResponse("Sorry page is not avaliable due to some internal problems")

class MyBlogs(ListView):
    template_name = "dashboard/my_blogs.html"
    model = BlogsModel
    pk_url_kwarg = "pk"
    context_object_name = "object"
    paginate_by = 20

    def get_queryset(self):
        if self.request.user.is_authenticated:
            pk = self.request.user.id
        else:
            return HttpResponseRedirect(reverse_lazy("login"))
        model = self.model.objects.filter(user_id=pk)
        return model
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"blogs": self.get_queryset()})
        return context

    def get(self, request: HttpRequest, *args, **kwargs):
        try:
            self.object_list = self.get_queryset()
            return self.render_to_response(self.get_context_data(**kwargs))
        except Exception:
            return HttpResponse("Sorry page is not avaliable due to some internal problems")