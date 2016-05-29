# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from modeltranslation.translator import translator, TranslationOptions
from models import File


class FileTranslationOptions(TranslationOptions):
    fields = ('comment',)


translator.register(File, FileTranslationOptions)
