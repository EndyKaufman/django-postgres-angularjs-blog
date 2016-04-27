# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-31 10:56
from __future__ import unicode_literals

from django.db import migrations
import json

def fill_from_mock(apps, schema_editor):

    try:
        with open('mock/tag/list.json') as f:
            content = f.read()
            f.close()
    except IOError:
        content = '[]'
    records = json.loads(content)

    Tag = apps.get_model("tag", "Tag")

    for record in records:
        tag, created = Tag.objects.get_or_create(text=record['text'])

class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fill_from_mock),
    ]
