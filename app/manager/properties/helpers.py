# -*- coding: utf-8 -*-
from project import helpers


def getListOfNames(names):
    list_of = getList()
    list_of_names = helpers.setNullValuesIfNotExist({}, names, '')
    if len(names) > 0:
        for item in list_of:
            for name in names:
                if item.name == name:
                    list_of_names[name] = item.value
    else:
        for item in list_of:
            list_of_names[item.name] = item.value
    return list_of_names


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
