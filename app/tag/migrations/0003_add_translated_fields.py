# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 16:00
from __future__ import unicode_literals

from django.db import migrations, models


def copy_to_translate(apps, schema_editor):
    from project import settings

    Tag = apps.get_model("tag", "Tag")
    fields = ['description']

    items = Tag.objects.all()
    for (lang, title) in settings.LANGUAGES:
        for item in items:
            for field in fields:
                setattr(item, '%s_%s' % (field, lang), getattr(item, field))
            item.save()


class Migration(migrations.Migration):
    dependencies = [
        ('tag', '0002_fill_from_mock'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='description_en',
            field=models.TextField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='description_ru',
            field=models.TextField(blank=True, max_length=512, null=True),
        ),
        migrations.RunPython(copy_to_translate),
    ]