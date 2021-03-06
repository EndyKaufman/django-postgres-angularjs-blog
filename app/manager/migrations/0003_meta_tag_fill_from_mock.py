# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-22 10:26
from __future__ import unicode_literals

from django.db import migrations
import json


def fill_from_mock(apps, schema_editor):
    try:
        with open('mock/manager/meta_tag_list.json') as f:
            content = f.read()
            f.close()
    except IOError:
        content = '[]'
    records = json.loads(content)

    MetaTag = apps.get_model("manager", "MetaTag")
    MetaTag.objects.all().delete()
    for record in records:
        item, created = MetaTag.objects.get_or_create(name=record['name'])
        item.content = record['content']
        item.attributes = record['attributes']
        item.save()


class Migration(migrations.Migration):
    dependencies = [
        ('manager', '0002_publiclink'),
    ]

    operations = [
        migrations.RunPython(fill_from_mock),
    ]
