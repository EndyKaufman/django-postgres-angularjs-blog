# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-24 14:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0005_add_fields_and_set_defaults'),
    ]

    operations = [
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=512, unique=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='date updated')),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
