# -*- coding: utf-8 -*-
from project import helpers
from django.db.models import Q


def update_from_json_data(request, project, json_data, user):
    from app.image.models import Image
    from app.tag.models import Tag

    try:
        project.title = json_data['title']
    except KeyError:
        project.title = None
    try:
        project.name = json_data['name']
    except KeyError:
        project.name = None
    try:
        project.description = json_data['description']
    except KeyError:
        project.description = None
    try:
        project.url = json_data['url']
    except KeyError:
        project.url = None
    try:
        project.text = json_data['text']
    except KeyError:
        project.text = None
    try:
        project.html = json_data['html']
    except KeyError:
        project.html = None
    try:
        project.markdown = json_data['markdown']
    except KeyError:
        project.markdown = None
    try:
        project.type = json_data['type']
    except KeyError:
        project.type = None

    if project.type == None:
        project.type = 1

    reload_source = {}

    # tags
    tagFieldIds = []
    tagFieldTexts = []
    for tag in json_data['tags']:
        try:
            tagId = tag['id']
        except KeyError:
            tagId = None
        try:
            tagText = tag['text']
        except KeyError:
            tagText = None
        if tagId is not None:
            tagFieldIds.append(tagId)
        if tagId is None and tagText is not None:
            tagFieldTexts.append(tag)

    for tag in project.tags.all():
        if tag.id not in tagFieldIds:
            project.tags.remove(tag)

    for tagText in tagFieldTexts:
        tag, tagCreated = Tag.objects.get_or_create(text=tagText['text'])
        if tagCreated:
            tag.created_user = user
            tag.save()
            reload_source['tag'] = True
        project.tags.add(tag)

    for tagId in tagFieldIds:
        tag = Tag.objects.get(pk=tagId)
        project.tags.add(tag)

    # images
    imageFieldIds = []
    imageFieldSrcs = []
    for image in json_data['images']:
        try:
            imageId = int(image['id'])
        except:
            imageId = None

        try:
            imageSrc = image['src']
        except KeyError:
            imageSrc = None
        if imageId is not None:
            imageFieldIds.append(imageId)

        if imageId is None and imageSrc is not None:
            imageFieldSrcs.append(image)

    for image in project.images.all():
        if image.id not in imageFieldIds:
            project.images.remove(image)

    for imageSrc in imageFieldSrcs:
        image, imageCreated = Image.objects.get_or_create(src=imageSrc['src'])
        if imageCreated:
            image.created_user = user
            image.save()
            reload_source['image'] = True
        project.images.add(image)

    for imageId in imageFieldIds:
        image = Image.objects.get(pk=imageId)
        project.images.add(image)

    project.save()

    return reload_source


def get_fields():
    return ['name', 'title', 'description']


def create(request):
    json_data = helpers.getJson(request)

    user = helpers.getUser(request)

    json_data = helpers.setNullValuesIfNotExist(json_data, get_fields())

    from app.project.models import Project

    item, created = Project.objects.get_or_create(name=json_data['name'], type=1, created_user=user)
    reload_source = []
    if created:
        reload_source = update_from_json_data(request, item, json_data, user)

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([item]), 'reload_source': reload_source}, 200, item


def update(request, project_id):
    """Update record"""

    json_data = helpers.getJson(request)

    user = helpers.getUser(request)

    json_data = helpers.setNullValuesIfNotExist(json_data, get_fields())

    from app.project.models import Project

    try:
        item = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return {'code': 'project/not_found', 'values': [project_id]}, 404, False

    reload_source = update_from_json_data(request, item, json_data, user)

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([item]), 'reload_source': reload_source}, 200, item


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

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([item])}, 200, item


def get_item_by_name(request, project_name):
    from app.project.models import Project

    try:
        item = Project.objects.get(name=project_name)
    except Project.DoesNotExist:
        return {'code': 'project/not_found', 'values': [project_name]}, 404, False

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([item])}, 200, item


def get_list(request):
    from app.project.models import Project

    items = Project.objects.all().order_by('-created').all()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(items)}, 200, items


def get_list_by_tag(request, tag_text):
    from app.project.models import Project

    items = Project.objects.filter(tags__text=tag_text).order_by('-created').all()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(items)}, 200, items


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

        return {'code': 'ok', 'data': helpers.itemsToJsonObject(items)}, 200, items
