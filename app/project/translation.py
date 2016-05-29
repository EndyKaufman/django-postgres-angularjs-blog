# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from modeltranslation.translator import translator, TranslationOptions
from models import Project


class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'text', 'html', 'markdown')


translator.register(Project, ProjectTranslationOptions)
