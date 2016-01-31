from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Tag model
class Tag(models.Model):
    text = models.TextField(max_length=512)
    description = models.TextField(max_length=512, blank=True, null=True)
