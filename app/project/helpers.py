# -*- coding: utf-8 -*-

def validate(jsonObject):
    try:
        nameField = jsonObject['name']
    except KeyError:
        return {'code': 'project/noname'}, 404
    try:
        titleField = jsonObject['title']
    except KeyError:
        return {'code': 'project/notitle'}, 404

    return {'code': 'ok'}, 200


def updateFromJsonObject(project, jsonObject, user):
    from app.image.models import Image
    from app.tag.models import Tag

    try:
        project.title = jsonObject['title']
    except KeyError:
        project.title = None
    try:
        project.name = jsonObject['name']
    except KeyError:
        project.name = None
    try:
        project.description = jsonObject['description']
    except KeyError:
        project.description = None
    try:
        project.url = jsonObject['url']
    except KeyError:
        project.url = None
    try:
        project.text = jsonObject['text']
    except KeyError:
        project.text = None
    try:
        project.html = jsonObject['html']
    except KeyError:
        project.html = None
    try:
        project.markdown = jsonObject['markdown']
    except KeyError:
        project.markdown = None
    try:
        project.type = jsonObject['type']
    except KeyError:
        project.type = None

    if project.type == None:
        project.type = 1

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

    return {'code': 'ok', 'reload_source': reload_source}, 200
