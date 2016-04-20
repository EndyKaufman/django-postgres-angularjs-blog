# -*- coding: utf-8 -*-


def validate(jsonObject):
    try:
        nameField = jsonObject['name']
    except KeyError:
        return {'code': 'post/noname'}, 404
    try:
        titleField = jsonObject['title']
    except KeyError:
        return {'code': 'post/notitle'}, 404

    return {'code': 'ok'}, 200


def updateFromJsonObject(post, jsonObject, user):
    from app.image.models import Image
    from app.tag.models import Tag

    try:
        post.title = jsonObject['title']
    except KeyError:
        post.title = None
    try:
        post.name = jsonObject['name']
    except KeyError:
        post.name = None
    try:
        post.description = jsonObject['description']
    except KeyError:
        post.description = None
    try:
        post.url = jsonObject['url']
    except KeyError:
        post.url = None
    try:
        post.text = jsonObject['text']
    except KeyError:
        post.text = None
    try:
        post.html = jsonObject['html']
    except KeyError:
        post.html = None
    try:
        post.markdown = jsonObject['markdown']
    except KeyError:
        post.markdown = None
    try:
        post.type = jsonObject['type']
    except KeyError:
        post.type = None

    if post.type == None:
        post.type = 1

    reload_source = {}

    # tags
    tagFieldIds = []
    tagFieldTexts = []
    for tag in jsonObject['tags']:
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
    for image in jsonObject['images']:
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

    return {'code': 'ok', 'reload_source': reload_source}, 200
