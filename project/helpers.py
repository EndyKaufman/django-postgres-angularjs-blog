# -*- coding: utf-8 -*-
import json
from django.core import serializers
import inspect


def is_method(obj, name):
    return hasattr(obj, name) and inspect.ismethod(getattr(obj, name))


def itemsToJsonObject(items):
    json_items = serializers.serialize('json', items)
    data = json.loads(json_items)
    results = []
    index = 0
    for row in data:
        result = row['fields']
        result['id'] = row['pk']
        for key in result:
            if hasattr(getattr(items[index], key), 'all'):
                result[key] = itemsToJsonObject(getattr(items[index], key).all())
        results.append(result)
        index = index + 1
    return results
