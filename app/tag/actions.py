# -*- coding: utf-8 -*-

from jsonview.decorators import json_view
from project import helpers


# list
@json_view
def getList(request):
    """List data"""

    from app.tag.models import Tag

    data = Tag.objects.all().order_by('-created').all()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}
