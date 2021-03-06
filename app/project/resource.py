# -*- coding: utf-8 -*-
from project import helpers
from models import Project


def update_from_json_data(request, item, data, user):
    from ..image.models import Image
    from ..tag.models import Tag

    helpers.json_to_objects(item, data)

    if item.type is None:
        item.type = 1

    reload_source = {}

    # tags
    tag_field_ids = []
    tag_field_texts = []
    for tag in data['tags']:
        try:
            tag_id = tag['id']
        except KeyError:
            tag_id = None
        try:
            tag_text = tag['text']
        except KeyError:
            tag_text = None
        if tag_id is not None:
            tag_field_ids.append(tag_id)
        if tag_id is None and tag_text is not None:
            tag_field_texts.append(tag)

    for tag in item.tags.all():
        if tag.id not in tag_field_ids:
            item.tags.remove(tag)

    for tag_text in tag_field_texts:
        tag, tag_created = Tag.objects.get_or_create(text=tag_text['text'])
        if tag_created:
            tag.created_user = user
            tag.save()
            reload_source['tag'] = True
        item.tags.add(tag)

    for tag_id in tag_field_ids:
        tag = Tag.objects.get(pk=tag_id)
        item.tags.add(tag)

    # images
    image_field_ids = []
    image_field_srcs = []
    for image in data['images']:
        try:
            image_id = int(image['id'])
        except:
            image_id = None

        try:
            image_src = image['src']
        except KeyError:
            image_src = None
        if image_id is not None:
            image_field_ids.append(image_id)

        if image_id is None and image_src is not None:
            image_field_srcs.append(image)

    for image in item.images.all():
        if image.id not in image_field_ids:
            item.images.remove(image)

    for image_src in image_field_srcs:
        image, image_created = Image.objects.get_or_create(src=image_src['src'])
        if image_created:
            image.created_user = user
            image.save()
            reload_source['image'] = True
        item.images.add(image)

    for image_id in image_field_ids:
        image = Image.objects.get(pk=image_id)
        item.images.add(image)

    item.save()

    return reload_source


def get_fields():
    return [f.name for f in Project._meta.get_fields()]


def create(request):
    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    item, created = Project.objects.get_or_create(name=data['name'], type=1, created_user=user)
    reload_source = []
    if created:
        reload_source = update_from_json_data(request, item, data, user)

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item]), 'reload_source': reload_source}, 200, item


def update(request, project_id):
    """Update record"""

    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    try:
        item = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return {'code': 'project/not_found', 'values': [project_id]}, 404, False

    reload_source = update_from_json_data(request, item, data, user)

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item]), 'reload_source': reload_source}, 200, item


def delete(request, project_id):
    """Update record"""
    try:
        item = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return {'code': 'project/not_found', 'values': [project_id]}, 404

    item.delete()

    return {'code': 'ok'}, 200


def get_item(request, project_id):
    try:
        item = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return {'code': 'project/not_found', 'values': [project_id]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_object_by_name(request, project_name):
    try:
        item = Project.objects.get(name=project_name)
    except Project.DoesNotExist:
        item = False
    return item


def get_item_by_name(request, project_name):
    try:
        item = Project.objects.get(name=project_name)
    except Project.DoesNotExist:
        return {'code': 'project/not_found', 'values': [project_name]}, 404, False
    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_list(request):
    items = Project.objects.all().order_by('-created').all()
    return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items


def get_list_by_tag(request, tag_text):
    items = Project.objects.filter(tags__text=tag_text).order_by('-created').all()
    return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items


def get_search(request, search_text):
    if search_text == 'all':
        return get_list(request)
    else:
        items = Project.objects.filter(
            helpers.get_searching_all_fields_qs(Project, search_text)
        ).order_by('-created').all()

        return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items
