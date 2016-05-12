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
import os
import shutil
from transliterate import slugify


def is_method(obj, name):
    return hasattr(obj, name) and inspect.ismethod(getattr(obj, name))


def get_user(request):
    if not request.user.is_authenticated():
        return False

    from app.account.models import User

    try:
        user = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        return None

    return user


def get_value_by_key(obj, key):
    try:
        value = obj[key]
    except:
        value = None

    return value


def set_null_values_if_not_exist(data, keys, null_value=None):
    for key in keys:
        try:
            value = data[key]
        except:
            value = null_value
        data[key] = value
    return data


def get_thumbnail(src):
    import re

    size = 250

    r_image = re.compile(r".*\.(jpg|png|gif)$")
    if not r_image.match(src):
        return False

    from easy_thumbnails.files import get_thumbnailer
    try:
        thumbnailer = get_thumbnailer(src)
        thumbnail_options = {'upscale': True}
        thumbnail_options['size'] = (size, 0)
        thumb = thumbnailer.get_thumbnail(thumbnail_options)
        return thumb
    except:
        return False


def mkdir_recursive(path, remove_if_exists=False):
    if remove_if_exists and os.path.isdir(path):
        shutil.rmtree(path)
    if not os.path.isdir(path):
        os.makedirs(path)


def copy_dir_recursive(src, dest, ignore=None, remove_if_exists=False):
    if os.path.isdir(src):
        mkdir_recursive(dest, remove_if_exists)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                copy_dir_recursive(os.path.join(src, f),
                                   os.path.join(dest, f),
                                   ignore, remove_if_exists)
    else:
        shutil.copyfile(src, dest)


def remove_file(path):
    if os.path.isfile(path):
        thumbnail = get_thumbnail(path)
        if thumbnail:
            os.remove(thumbnail.url)
        os.remove(path)
    else:
        path = settings.MEDIA_ROOT + '/' + path
        thumbnail = get_thumbnail(path)
        if thumbnail:
            os.remove(thumbnail.url)
        if os.path.isfile(path):
            os.remove(path)


def save_file(dest_path, f, filename=False):
    original_name, file_extension = os.path.splitext(f.name)

    filename_postfix_inc = 1
    def_filename = False
    while True:
        if filename is not False:
            new_filename = u'%s' % filename
        else:
            new_filename = u'%s' % original_name

        if def_filename is False:
            def_filename = new_filename

        if dest_path is False:
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
            filename_postfix_inc += 1
            filename = '%s-%s' % (def_filename, str(filename_postfix_inc))

    if dest_path == False:
        mkdir_recursive(settings.MEDIA_ROOT)
    else:
        mkdir_recursive(settings.MEDIA_ROOT + '/' + dest_path)

    destination = open(path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    return url


def md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()


def make_code(size=6, chars=string.ascii_uppercase + string.digits):
    random.seed()
    return ''.join(random.choice(chars) for _ in range(size)).lower()


def send_mail(subject, text_content, html_content=None, to_email=None, message_id=None):
    from_email = '%s <%s>' % (settings.SITE_NAME, settings.SERVER_EMAIL)

    if to_email is None:
        to_email = [settings.SERVER_EMAIL]

    msg = EmailMultiAlternatives(subject, '', from_email, to_email)
    if html_content is not None:
        msg.attach_alternative(html_content, "text/html")
        msg.content_subtype = "html"  # Main content is now text/html

    try:
        msg.send()
    except:
        temp_dir = '%s/%s' % (os.path.dirname(settings.BASE_DIR), 'temp')
        temp_file = "%s/%s.html" % (temp_dir, to_email[0].encode('ascii', 'ignore'))

        mkdir_recursive(temp_dir)
        with open(temp_file, "w") as text_file:
            text_file.write("<!-- From: %s, To: %s, Subject: %s !-->%s" % (
                from_email, to_email[0].encode('ascii', 'ignore'), subject, html_content))
    return True


def objects_to_json(request, items):
    json_items = serializers.serialize('json', items)
    data = json.loads(json_items)

    results = []
    index = 0
    for row in data:
        result = row['fields']
        result['id'] = row['pk']
        static_fields = ['src']

        for static_field in static_fields:
            try:
                field_value = result[static_field]
            except:
                field_value = None
            if field_value is not None and field_value != '':
                if '//' in field_value.lower():
                    try:
                        result['%s_url' % static_field] = field_value
                    except:
                        result['%s_url' % static_field] = ''
                else:
                    try:
                        result['%s_url' % static_field] = 'http://%s%s%s' % (
                            request.get_host(), settings.MEDIA_URL, field_value)
                        thumbnail = get_thumbnail(field_value)
                        if thumbnail:
                            result['%s_thumbnail_url' % static_field] = 'http://%s%s%s' % (
                                request.get_host(), settings.MEDIA_URL, thumbnail)
                    except:
                        result['%s_url' % static_field] = ''

        for key in result:
            if hasattr(items[index], key) and hasattr(getattr(items[index], key), 'all'):
                result[key] = objects_to_json(request, getattr(items[index], key).all())
        results.append(result)
        index += 1

    return results
