# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-31 16:13
from __future__ import unicode_literals

from django.db import migrations
from project import helpers
import json


def fill_from_mock(apps, schema_editor):
    helpers.copydirRecursive('mock/file/media', 'project/media', removeIfExists=True)
    try:
        with open('mock/file/list.json') as f:
            content = f.read()
            f.close()
    except IOError:
        content = '[]'
    records = json.loads(content)

    File = apps.get_model("file", "File")

    for record in records:
        file, created = File.objects.get_or_create(pk=record['id'], src=record['src'], comment=record['comment'])


class Migration(migrations.Migration):
    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fill_from_mock),
    ]