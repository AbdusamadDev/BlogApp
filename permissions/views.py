from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from typing import Optional

class IsAuthenticatedMixin(LoginRequiredMixin):
    request = None

    def test_func(self) -> Optional[bool]:
        assert self.request is None, """Nonetype object has no attribute user"""
        if not self.request.user.is_authenticated:
            return self.handle_no_permission()

    def handle_no_permission(self) -> HttpResponseRedirect:
        if self.login_url is None:
            return "Please specify login_url attribute"
        return HttpResponseRedirect(reverse_lazy("login"))
