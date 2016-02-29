from __future__ import unicode_literals
from django.conf import settings
from django.db import models


# File model
class File(models.Model):
    comment = models.TextField(max_length=512, blank=True, null=True)
    src = models.TextField(max_length=1024, blank=True, null=True)
    created = models.DateTimeField('date created', auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField('date updated', auto_now=True, blank=True, null=True)
    created_user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
