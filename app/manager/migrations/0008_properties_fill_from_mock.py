# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-25 05:59
from __future__ import unicode_literals

from django.db import migrations
import json
from project import helpers


def fill_from_mock(apps, schema_editor):
    try:
        with open('mock/manager/properties_list.json') as f:
            content = f.read()
            f.close()
    except IOError:
        content = '[]'
    records = json.loads(content)

    Properties = apps.get_model("manager", "Properties")
    Properties.objects.all().delete()
    for record in records:
        record = helpers.setNullValuesIfNotExist(record, ['name', 'value', 'comment', 'only_update'])
        item, created = Properties.objects.get_or_create(name=record['name'])
        item.value = record['value']
        item.comment = record['comment']
        item.only_update = record['only_update']
        item.save()


class Migration(migrations.Migration):
    dependencies = [
        ('manager', '0007_add_field_to_properties'),
    ]

    operations = [
        migrations.RunPython(fill_from_mock),
    ]