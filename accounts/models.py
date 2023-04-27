from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

CHOICES = (
    ("Male", "Male"),
    ("Female", "Female")
)

# avatar, date_of_birth, gender, date_joined
class UserProfile(AbstractUser):
    bio = models.CharField(max_length=500)
    avatar = models.ImageField(upload_to="avatars/")
    date_joined = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=10, choices=CHOICES)
    birthdate = models.DateTimeField()
    groups = models.ManyToManyField(Group, related_name='user_profiles')
    user_permissions = models.ManyToManyField(Permission, related_name='user_profiles')

    def __str__(self) -> str:
        return str((self.username, self.email, self.password, self.bio))
    
# HINT: Add or change a related_name argument 
# to the definition for 'auth.User.user_permissions' or 'accounts.UserProfile.user_permissions'.
# issue___________________________________________________

