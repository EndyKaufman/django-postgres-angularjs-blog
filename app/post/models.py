from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from ..image.models import Image
from ..tag.models import Tag


# Post model
class Post(models.Model):
    title = models.TextField(max_length=512)
    name = models.TextField(max_length=512, unique=True)
    description = models.TextField(max_length=512, blank=True, null=True)
    url = models.TextField(max_length=1024, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    markdown = models.TextField(blank=True, null=True)
    type = models.IntegerField()
    images = models.ManyToManyField(Image, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created = models.DateTimeField('date created', auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField('date updated', auto_now=True, blank=True, null=True)
    created_user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
