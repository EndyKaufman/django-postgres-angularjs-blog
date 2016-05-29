# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from modeltranslation.translator import translator, TranslationOptions
from models import Post


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'text', 'html', 'markdown')


translator.register(Post, PostTranslationOptions)
