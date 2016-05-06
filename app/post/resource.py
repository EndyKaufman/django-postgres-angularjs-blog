# -*- coding: utf-8 -*-
from project import helpers
from django.db.models import Q


def update_from_json_data(post, json_data, user):
    from app.image.models import Image
    from app.tag.models import Tag

    try:
        post.title = json_data['title']
    except KeyError:
        post.title = None
    try:
        post.name = json_data['name']
    except KeyError:
        post.name = None
    try:
        post.description = json_data['description']
    except KeyError:
        post.description = None
    try:
        post.url = json_data['url']
    except KeyError:
        post.url = None
    try:
        post.text = json_data['text']
    except KeyError:
        post.text = None
    try:
        post.html = json_data['html']
    except KeyError:
        post.html = None
    try:
        post.markdown = json_data['markdown']
    except KeyError:
        post.markdown = None
    try:
        post.type = json_data['type']
    except KeyError:
        post.type = None

    if post.type == None:
        post.type = 1

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

    for tag in post.tags.all():
        if tag.id not in tagFieldIds:
            post.tags.remove(tag)

    for tagText in tagFieldTexts:
        tag, tagCreated = Tag.objects.get_or_create(text=tagText['text'])
        if tagCreated:
            tag.created_user = user
            tag.save()
            reload_source['tag'] = True
        post.tags.add(tag)

    for tagId in tagFieldIds:
        tag = Tag.objects.get(pk=tagId)
        post.tags.add(tag)

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

    for image in post.images.all():
        if image.id not in imageFieldIds:
            post.images.remove(image)

    for imageSrc in imageFieldSrcs:
        image, imageCreated = Image.objects.get_or_create(src=imageSrc['src'])
        if imageCreated:
            image.created_user = user
            image.save()
            reload_source['image'] = True
        post.images.add(image)

    for imageId in imageFieldIds:
        image = Image.objects.get(pk=imageId)
        post.images.add(image)

    return reload_source


def create(request):
    json_data = helpers.getJson(request)

    user = helpers.getUser(request)

    json_data = helpers.setNullValuesIfNotExist(json_data, ['name', 'title'])

    from app.post.models import Post

    item, created = Post.objects.get_or_create(name=json_data['name'], type=1, created_user=user)
    reload_source = []
    if created:
        reload_source = update_from_json_data(item, json_data, user)
        item.save()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([item]), 'reload_source': reload_source}, 200, item


def update(request, post_id):
    """Update record"""

    json_data = helpers.getJson(request)

    user = helpers.getUser(request)

    json_data = helpers.setNullValuesIfNotExist(json_data, ['name', 'title'])

    from app.post.models import Post

    try:
        item = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return {'code': 'post/not_found', 'values': [post_id]}, 404, False

    reload_source = update_from_json_data(item, json_data, user)
    item.save()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([item]), 'reload_source': reload_source}, 200, item


def delete(request, post_id):
    """Update record"""

    from app.post.models import Post

    try:
        item = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return {'code': 'post/not_found', 'values': [post_id]}, 404

    item.delete()

    return {'code': 'ok'}, 200


def get_item(request, post_id):
    from app.post.models import Post

    try:
        item = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return {'code': 'post/not_found', 'values': [post_id]}, 404, False

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([item])}, 200, item


def get_item_by_name(request, post_name):
    from app.post.models import Post

    try:
        item = Post.objects.get(name=post_name)
    except Post.DoesNotExist:
        return {'code': 'post/not_found', 'values': [post_name]}, 404, False

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([item])}, 200, item


def get_list(request):
    from app.post.models import Post

    items = Post.objects.all().order_by('-created').all()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(items)}, 200, items


def get_list_by_tag(request, tag_text):
    from app.post.models import Post

    items = Post.objects.filter(tags__text=tag_text).order_by('-created').all()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(items)}, 200, items


def get_search(request, search_text):
    if search_text == 'all':
        return get_list(request)
    else:
        from app.post.models import Post

        items = Post.objects.filter(
            Q(title__icontains=search_text) |
            Q(name__icontains=search_text) |
            Q(description__icontains=search_text) |
            Q(url__icontains=search_text) |
            Q(text__icontains=search_text) |
            Q(html__icontains=search_text) |
            Q(markdown__icontains=search_text)
        ).order_by('-created').all()

        return {'code': 'ok', 'data': helpers.itemsToJsonObject(items)}, 200, items
