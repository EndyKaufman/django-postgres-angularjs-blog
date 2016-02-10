# -*- coding: utf-8 -*-
from django.core import serializers
from django.contrib.staticfiles.templatetags.staticfiles import static
import json
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
        staticFields = ['src']

        for staticField in staticFields:
            try:
                fieldValue = result[staticField]
            except:
                fieldValue = None
            if fieldValue is not None and fieldValue != '' and 'http:' not in fieldValue.lower():
                try:
                    result['%sStatic' % staticField] = static(fieldValue)
                except:
                    result['%sStatic' % staticField] = ''

        for key in result:
            if hasattr(items[index], key) and hasattr(getattr(items[index], key), 'all'):
                result[key] = itemsToJsonObject(getattr(items[index], key).all())
        results.append(result)
        index = index + 1

    return results
