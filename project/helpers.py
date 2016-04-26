# -*- coding: utf-8 -*-
from django.core import serializers
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import os
import json
import inspect
import string
import random
import hashlib
import os.path
import shutil
from transliterate import slugify


def is_method(obj, name):
    return hasattr(obj, name) and inspect.ismethod(getattr(obj, name))


def getUser(request):
    if not request.user.is_authenticated():
        return False

    from app.account.models import User

    try:
        user = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        return None

    return user


def getValueByKey(obj, key):
    try:
        value = obj[key]
    except:
        value = None

    return value


def setNullValuesIfNotExist(data, keys, null_value=None):
    for key in keys:
        try:
            value = data[key]
        except:
            value = null_value
        data[key] = value
    return data


def getJson(request):
    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    return json_data


def mkdirRecursive(path, removeIfExists=False):
    if removeIfExists and os.path.isdir(path):
        shutil.rmtree(path)
    if not os.path.isdir(path):
        os.makedirs(path)


def copydirRecursive(src, dest, ignore=None, removeIfExists=False):
    if os.path.isdir(src):
        mkdirRecursive(dest, removeIfExists)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                copydirRecursive(os.path.join(src, f),
                                 os.path.join(dest, f),
                                 ignore, removeIfExists)
    else:
        shutil.copyfile(src, dest)


def removeFile(path):
    if os.path.isfile(path):
        os.remove(path)
    else:
        path = settings.MEDIA_ROOT + '/' + path
        if os.path.isfile(path):
            os.remove(path)


def saveFile(dest_path, f, filename=False):
    original_name, file_extension = os.path.splitext(f.name)

    filename_postfix_inc = 1
    def_filename = False
    while True:
        if filename != False:
            new_filename = u'%s' % filename
        else:
            new_filename = u'%s' % original_name

        if def_filename == False:
            def_filename = new_filename;

        if dest_path == False:
            try:
                url = slugify(new_filename) + file_extension
            except:
                url = new_filename + file_extension
            path = settings.MEDIA_ROOT + '/' + url
        else:
            url = dest_path + '/' + slugify(new_filename) + file_extension
            path = settings.MEDIA_ROOT + '/' + url

        if os.path.isfile(path) == False:
            break

        if os.path.isfile(path):
            filename_postfix_inc = filename_postfix_inc + 1
            filename = '%s-%s' % (def_filename, str(filename_postfix_inc))

    if dest_path == False:
        mkdirRecursive(settings.MEDIA_ROOT)
    else:
        mkdirRecursive(settings.MEDIA_ROOT + '/' + dest_path)

    destination = open(path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    return url


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

    msg = EmailMultiAlternatives(subject, '', from_email, to_email)
    if html_content != None:
        msg.attach_alternative(html_content, "text/html")
        msg.content_subtype = "html"  # Main content is now text/html

    try:
        msg.send()
    except:
        tempDir = '%s/%s' % (os.path.dirname(settings.BASE_DIR), 'temp')
        tempFile = "%s/%s.html" % (tempDir, to_email[0].encode('ascii', 'ignore'))

        mkdirRecursive(tempDir)
        with open(tempFile, "w") as text_file:
            text_file.write("<!-- From: %s, To: %s, Subject: %s !-->%s" % (
                from_email, to_email[0].encode('ascii', 'ignore'), subject, html_content))
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
                    result['%sStatic' % staticField] = '%s%s' % (settings.MEDIA_URL, fieldValue)
                except:
                    result['%sStatic' % staticField] = ''

        for key in result:
            if hasattr(items[index], key) and hasattr(getattr(items[index], key), 'all'):
                result[key] = itemsToJsonObject(getattr(items[index], key).all())
        results.append(result)
        index = index + 1

    return results
