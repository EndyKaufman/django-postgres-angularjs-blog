from __future__ import unicode_literals
from django.conf import settings
from django.db import models


# MetaTag model
class MetaTag(models.Model):
    name = models.TextField(max_length=512, unique=True)
    content = models.TextField(max_length=512, blank=True, null=True)
    attributes = models.TextField(max_length=1024, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField('date created', auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField('date updated', auto_now=True, blank=True, null=True)
    created_user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)


# PublicLink model
class PublicLink(models.Model):
    src = models.TextField(max_length=1024, unique=True)
    title = models.TextField(max_length=512, blank=True, null=True)
    description = models.TextField(max_length=1024, blank=True, null=True)
    icon = models.TextField(max_length=512, blank=True, null=True)
    in_header = models.IntegerField(default=0)
    in_contact = models.IntegerField(default=0)
    in_footer = models.IntegerField(default=0)
    position = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField('date created', auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField('date updated', auto_now=True, blank=True, null=True)
    created_user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)

# Properties model
class Properties(models.Model):
    name = models.TextField(max_length=512, unique=True)
    value = models.TextField(blank=True, null=True)
    created = models.DateTimeField('date created', auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField('date updated', auto_now=True, blank=True, null=True)
    created_user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)