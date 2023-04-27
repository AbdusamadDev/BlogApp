from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import UserProfile


admin.site.register(UserProfile, UserAdmin)
