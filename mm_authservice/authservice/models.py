from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.


class User(AbstractUser):
    UserID = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    first_name = models.TextField()
    last_name = models.TextField()
    username = models.CharField(max_length=255, unique=True)
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

    def __str__(self):
        return self.username