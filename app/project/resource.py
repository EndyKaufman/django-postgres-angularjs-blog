# -*- coding: utf-8 -*-
from project import helpers
from django.db.models import Q


def update_from_json_data(request, item, data, user):
    from app.image.models import Image
    from app.tag.models import Tag

    if data['title'] is not None:
        item.title = data['title']
    if data['name'] is not None:
        item.name = data['name']
    if data['description'] is not None:
        item.description = data['description']
    if data['url'] is not None:
        item.url = data['url']
    if data['text'] is not None:
        item.text = data['text']
    if data['html'] is not None:
        item.html = data['html']
    if data['markdown'] is not None:
        item.markdown = data['markdown']
    if data['type'] is not None:
        item.type = data['type']

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
    return ['name', 'title', 'description', 'url', 'text', 'html', 'markdown', 'type']


def create(request):
    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    from app.project.models import Project

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

    from app.project.models import Project

    try:
        item = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return {'code': 'project/not_found', 'values': [project_id]}, 404, False

    reload_source = update_from_json_data(request, item, data, user)

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item]), 'reload_source': reload_source}, 200, item


def delete(request, project_id):
    """Update record"""

    from app.project.models import Project

    try:
        item = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return {'code': 'project/not_found', 'values': [project_id]}, 404

    item.delete()

    return {'code': 'ok'}, 200


def get_item(request, project_id):
    from app.project.models import Project

    try:
        item = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return {'code': 'project/not_found', 'values': [project_id]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_item_by_name(request, project_name):
    from app.project.models import Project

    try:
        item = Project.objects.get(name=project_name)
    except Project.DoesNotExist:
        return {'code': 'project/not_found', 'values': [project_name]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_list(request):
    from app.project.models import Project

    items = Project.objects.all().order_by('-created').all()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items


def get_list_by_tag(request, tag_text):
    from app.project.models import Project

    items = Project.objects.filter(tags__text=tag_text).order_by('-created').all()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items


def get_search(request, search_text):
    if search_text == 'all':
        return get_list(request)
    else:
        from app.project.models import Project

        items = Project.objects.filter(
            Q(title__icontains=search_text) |
            Q(name__icontains=search_text) |
            Q(description__icontains=search_text) |
            Q(url__icontains=search_text) |
            Q(text__icontains=search_text) |
            Q(html__icontains=search_text) |
            Q(markdown__icontains=search_text)
        ).order_by('-created').all()

        return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items
