from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


# User model
class User(AbstractUser):
    def get_user_data(self):

        roles = []

        if self.is_staff:
            roles.append('user')
        if self.is_superuser:
            roles.append('admin')

        if len(roles) == 0:
            return {}

        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "firstname": self.first_name,
            "lastname": self.last_name,
            "roles": roles
        }


# Code model
class Code(models.Model):
    text = models.TextField(max_length=512)
    type = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField('date created', auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField('date updated', auto_now=True, blank=True, null=True)
    created_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
