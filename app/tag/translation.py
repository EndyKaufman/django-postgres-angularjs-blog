# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from modeltranslation.translator import translator, TranslationOptions
from models import Tag


class TagTranslationOptions(TranslationOptions):
    fields = ('description', )


translator.register(Tag, TagTranslationOptions)
