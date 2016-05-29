# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from modeltranslation.translator import translator, TranslationOptions
from models import Image


class ImageTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Image, ImageTranslationOptions)
