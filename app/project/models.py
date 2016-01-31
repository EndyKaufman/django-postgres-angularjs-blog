from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from app.image.models import Image
from app.tag.models import Tag

# Project model
class Project(models.Model):
    title = models.TextField(max_length=512)
    name = models.TextField(max_length=512)
    description = models.TextField(max_length=512, blank=True, null=True)
    url = models.TextField(max_length=1024, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    markdown = models.TextField(blank=True, null=True)
    type = models.IntegerField()

# Project images link model
class Image_Links(models.Model):
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL)
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.SET_NULL)

# Project tags link model
class Tag_Links(models.Model):
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL)
    tag = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.SET_NULL)