# -*- coding: utf-8 -*-

def getList():
    from app.tag.models import Tag

    try:
        data = Tag.objects.order_by('created').all()
    except Tag.DoesNotExist:
        data = []
    return data


def getItem(id):
    from app.tag.models import Tag

    try:
        data = [Tag.objects.get(pk=id)]
    except Tag.DoesNotExist:
        data = False
    return data


def getItemByText(text):
    from app.tag.models import Tag

    try:
        data = [Tag.objects.get(text=text)]
    except Tag.DoesNotExist:
        data = False
    return data


def create(data):
    from app.tag.models import Tag

    try:
        return [Tag.objects.create(text=data['text'], description=data['description'])]
    except:
        return False
