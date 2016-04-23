# -*- coding: utf-8 -*-

def getList():
    from app.manager.models import PublicLink

    try:
        data = PublicLink.objects.order_by('position').all()
    except PublicLink.DoesNotExist:
        data = []
    return data


def getItem(id):
    from app.manager.models import PublicLink

    try:
        data = [PublicLink.objects.get(pk=id)]
    except PublicLink.DoesNotExist:
        data = False
    return data


def getItemBySrc(src):
    from app.manager.models import PublicLink

    try:
        data = [PublicLink.objects.get(src=src)]
    except PublicLink.DoesNotExist:
        data = False
    return data


def create(data):
    from app.manager.models import PublicLink

    try:
        return [PublicLink.objects.create(src=data['src'], title=data['title'],
                                          icon=data['icon'], in_header=data['in_header'], in_footer=data['in_footer'],
                                          position=data['position'],
                                          in_contact=data['in_contact'])]
    except:
        return False
