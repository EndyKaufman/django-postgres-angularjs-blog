# -*- coding: utf-8 -*-

import json
from jsonview.decorators import json_view
from project import helpers
from helpers import updateFromJsonObject, validate
from django.db.models import Q


# list
@json_view
def getList(request):
    """List data"""

    from app.post.models import Post

    data = Post.objects.all().order_by('-created').all()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# search
@json_view
def getSearch(request, search_text):
    """Search data"""
    if search_text == 'all':
        return getList(request)
    else:
        from app.post.models import Post

        data = Post.objects.filter(
            Q(title__icontains=search_text) |
            Q(name__icontains=search_text) |
            Q(description__icontains=search_text) |
            Q(url__icontains=search_text) |
            Q(text__icontains=search_text) |
            Q(html__icontains=search_text) |
            Q(markdown__icontains=search_text)
        ).order_by('-created').all()

        return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# search by tag
@json_view
def getListByTag(request, tag_text):
    """List data by tag"""

    from app.post.models import Post

    data = Post.objects.filter(tags__text=tag_text).order_by('-created').all()

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# item
@json_view
def getItem(request, post_name):
    """Item data"""

    from app.post.models import Post

    try:
        data = [Post.objects.get(name=post_name)]
    except Post.DoesNotExist:
        return {'code': 'post/notfound', 'values': [post_name]}, 404

    return {'code': 'ok', 'data': helpers.itemsToJsonObject(data)}


# update
@json_view
def actionUpdate(request, post_id):
    """Update record"""

    if not request.user.is_authenticated() or not request.user.is_superuser:
        return {'code': 'noaccess'}, 404

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    from app.account.models import User

    try:
        user = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        return {'code': 'account/younotactive'}, 404

    from app.post.models import Post

    validateResult, validateCode = validate(json_data)

    if validateCode != 200:
        return validateResult, validateCode

    try:
        post = Post.objects.get(name=json_data['name'])
    except Post.DoesNotExist:
        post = False

    if (post is not False) and (int(post.id) != int(post_id)):
        return {'code': 'post/exists', 'values': [json_data['name'], post.id]}, 404

    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return {'code': 'post/notfound', 'values': [post_id]}, 404

    # try:
    updateResult, updateCode = updateFromJsonObject(post, json_data, user)
    if updateCode != 200:
        return updateResult, updateCode
    post.save()
    # except:
    #    return {'code': 'post/update/fail'}, 404

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([post]), 'reload_source': updateResult['reload_source']}


# create
@json_view
def actionCreate(request):
    """Create record"""

    if not request.user.is_authenticated() or not request.user.is_superuser:
        return {'code': 'noaccess'}, 404

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    from app.account.models import User

    try:
        user = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        return {'code': 'account/younotactive'}, 404

    from app.post.models import Post

    validateResult, validateCode = validate(json_data)

    if validateCode != 200:
        return validateResult, validateCode

    try:
        post = Post.objects.get(name=json_data['name'])
    except Post.DoesNotExist:
        post = False

    if post is not False:
        return {'code': 'post/exists', 'values': [json_data['name']]}, 404

    post = Post.objects.create(name=json_data['name'], type=1, created_user=user)

    # try:
    createResult, createCode = updateFromJsonObject(post, json_data, user)
    if createCode != 200:
        return createResult, createCode
    post.save()
    # except:
    #     return {'code': 'post/create/fail'}, 404

    return {'code': 'ok', 'data': helpers.itemsToJsonObject([post]), 'reload_source': createResult['reload_source']}


# delete
@json_view
def actionDelete(request, post_id):
    """Delete record"""

    if not request.user.is_authenticated() or not request.user.is_superuser:
        return {'code': 'noaccess'}, 404

    json_data = False

    if request.method == 'POST':
        json_data = json.loads(request.body)

    if json_data is False:
        return {'code': 'nodata'}, 404

    from app.account.models import User

    try:
        user = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        return {'code': 'account/younotactive'}, 404

    from app.post.models import Post

    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return {'code': 'post/notfound', 'values': [post_id]}, 404

    try:
        post.delete()
    except:
        return {'code': 'post/fail/delete'}, 404

    return {'code': 'ok'}
