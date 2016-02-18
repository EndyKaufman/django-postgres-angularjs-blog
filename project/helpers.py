# -*- coding: utf-8 -*-
from django.core import serializers
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import json
import inspect
import string
import random
import hashlib


def is_method(obj, name):
    return hasattr(obj, name) and inspect.ismethod(getattr(obj, name))


def md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()


def makeCode(size=6, chars=string.ascii_uppercase + string.digits):
    random.seed()
    return ''.join(random.choice(chars) for _ in range(size)).lower()


def sendmail(subject, text_content, html_content=None, to_email=None, message_id=None):
    from_email = '%s <%s>' % (settings.SITE_NAME, settings.SERVER_EMAIL)

    if to_email == None:
        to_email = [settings.SERVER_EMAIL]

    msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    if html_content != None:
        msg.attach_alternative(html_content, "text/html")
        msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    return True


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
