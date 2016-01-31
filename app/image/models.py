from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Image model
class Image(models.Model):
    title = models.TextField(max_length=512)
    description = models.TextField(max_length=512, blank=True, null=True)
    src = models.TextField(max_length=1024, blank=True, null=True)