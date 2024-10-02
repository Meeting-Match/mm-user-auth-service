from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.


class User(AbstractUser):
    country = models.TextField()
    groups = models.ManyToManyField(
        Group,
        related_name='authservice_user_groups',  # Add a unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='authservice_user_permissions',  # Add a unique related_name
        blank=True
    )
