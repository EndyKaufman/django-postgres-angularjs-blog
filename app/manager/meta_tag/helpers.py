# -*- coding: utf-8 -*-

def getList():
    from app.manager.models import MetaTag

    try:
        data = MetaTag.objects.order_by('position').all()
    except MetaTag.DoesNotExist:
        data = []
    return data


def getItem(id):
    from app.manager.models import MetaTag

    try:
        data = [MetaTag.objects.get(pk=id)]
    except MetaTag.DoesNotExist:
        data = False
    return data


def getItemByName(name):
    from app.manager.models import MetaTag

    try:
        data = [MetaTag.objects.get(name=name)]
    except MetaTag.DoesNotExist:
        data = False
    return data


def create(data):
    from app.manager.models import MetaTag

    try:
        return [MetaTag.objects.create(name=data['name'], content=data['content'],
                                       attributes=data['attributes'],
                                       position=data['position'], created_user=data['created_user'])]
    except:
        return False
