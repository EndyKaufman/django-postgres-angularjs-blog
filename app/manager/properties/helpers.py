# -*- coding: utf-8 -*-

def getList():
    from app.manager.models import Properties

    try:
        data = Properties.objects.order_by('created').all()
    except Properties.DoesNotExist:
        data = []
    return data


def getItem(id):
    from app.manager.models import Properties

    try:
        data = [Properties.objects.get(pk=id)]
    except Properties.DoesNotExist:
        data = False
    return data


def getItemByName(name):
    from app.manager.models import Properties

    try:
        data = [Properties.objects.get(name=name)]
    except Properties.DoesNotExist:
        data = False
    return data


def create(data):
    from app.manager.models import Properties

    try:
        return [Properties.objects.create(name=data['name'], value=data['value'], comment=data['comment'],
                                          created_user=data['created_user'], only_update=0)]
    except:
        return False
