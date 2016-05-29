# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from modeltranslation.translator import translator, TranslationOptions
from models import Properties, PublicLink, MetaTag


class MetaTagTranslationOptions(TranslationOptions):
    fields = ('content', 'attributes')


class PublicLinkTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class PropertiesTranslationOptions(TranslationOptions):
    fields = ('comment', 'value')


translator.register(Properties, PropertiesTranslationOptions)

translator.register(PublicLink, PublicLinkTranslationOptions)

translator.register(MetaTag, MetaTagTranslationOptions)
