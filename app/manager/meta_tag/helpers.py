# -*- coding: utf-8 -*-

from app.manager.models import MetaTag


def getMetaTagList():
    try:
        list = MetaTag.objects.all()
    except MetaTag.DoesNotExist:
        list = []
    return list
