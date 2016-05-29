# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 16:00
from __future__ import unicode_literals

from django.db import migrations, models


def copy_to_translate(apps, schema_editor):
    from project import settings

    Project = apps.get_model("project", "Project")
    fields = ['title', 'description', 'text', 'html', 'markdown']

    items = Project.objects.all()
    for (lang, title) in settings.LANGUAGES:
        for item in items:
            for field in fields:
                setattr(item, '%s_%s' % (field, lang), getattr(item, field))
            item.save()


class Migration(migrations.Migration):
    dependencies = [
        ('project', '0002_fill_from_mock'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description_en',
            field=models.TextField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='description_ru',
            field=models.TextField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='html_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='html_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='markdown_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='markdown_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='text_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='text_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='title_en',
            field=models.TextField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='title_ru',
            field=models.TextField(max_length=512, null=True),
        ),
        migrations.RunPython(copy_to_translate),
    ]
