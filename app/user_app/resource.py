# -*- coding: utf-8 -*-
from project import helpers
from django.db.models import Q


def get_fields():
    return ['client_id', 'user', 'redirect_uris', 'client_type', 'authorization_grant_type', 'client_secret', 'name',
            'skip_authorization']


def create(request):
    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    from oauth2_provider.models import get_application_model
    from oauth2_provider.generators import generate_client_secret, generate_client_id
    from oauth2_provider.models import AbstractApplication

    data['client_type'] = AbstractApplication.CLIENT_CONFIDENTIAL
    data['authorization_grant_type'] = AbstractApplication.GRANT_PASSWORD
    data['skip_authorization'] = True
    data['client_id'] = generate_client_id()
    data['client_secret'] = generate_client_secret()

    item, created = get_application_model().objects.get_or_create(client_id=data['client_id'],
                                                                  user=user,
                                                                  redirect_uris=data['redirect_uris'],
                                                                  client_type=data['client_type'],
                                                                  authorization_grant_type=data[
                                                                      'authorization_grant_type'],
                                                                  client_secret=data['client_secret'],
                                                                  name=data['name'],
                                                                  skip_authorization=data['skip_authorization'])

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def update(request, user_app_id):
    """Update record"""

    data = request.DATA

    user = helpers.get_user(request)

    data = helpers.set_null_values_if_not_exist(data, get_fields())

    from oauth2_provider.models import get_application_model
    from oauth2_provider.generators import generate_client_secret, generate_client_id
    from oauth2_provider.models import AbstractApplication

    try:
        item = get_application_model().objects.get(pk=user_app_id)
    except get_application_model().DoesNotExist:
        return {'code': 'user_app/not_found', 'values': [user_app_id]}, 404, False

    data['client_type'] = AbstractApplication.CLIENT_CONFIDENTIAL
    data['authorization_grant_type'] = AbstractApplication.GRANT_PASSWORD
    data['skip_authorization'] = True
    data['client_id'] = generate_client_id()
    data['client_secret'] = generate_client_secret()

    # item.client_id = data['client_id']
    item.user = user
    if data['redirect_uris'] is not None:
        item.redirect_uris = data['redirect_uris']
    if data['client_type'] is not None:
        item.client_type = data['client_type']
    if data['authorization_grant_type'] is not None:
        item.authorization_grant_type = data['authorization_grant_type']
    # item.client_secret = data['client_secret']
    if data['name'] is not None:
        item.name = data['name']
    if data['skip_authorization'] is not None:
        item.skip_authorization = data['skip_authorization']
    item.save()

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def delete(request, user_app_id):
    """Update record"""

    from oauth2_provider.models import get_application_model

    try:
        item = get_application_model().objects.get(pk=user_app_id)
    except get_application_model().DoesNotExist:
        return {'code': 'user_app/not_found', 'values': [user_app_id]}, 404

    item.delete()

    return {'code': 'ok'}, 200


def get_item(request, user_app_id):
    from oauth2_provider.models import get_application_model

    try:
        item = get_application_model().objects.get(pk=user_app_id)
    except get_application_model().DoesNotExist:
        return {'code': 'user_app/not_found', 'values': [user_app_id]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_item_by_client_id(request, user_app_client_id):
    from oauth2_provider.models import get_application_model

    try:
        item = get_application_model().objects.get(client_id=user_app_client_id)
    except get_application_model().DoesNotExist:
        return {'code': 'user_app/not_found', 'values': [user_app_client_id]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_item_by_name(request, user_app_name):
    from oauth2_provider.models import get_application_model

    try:
        item = get_application_model().objects.get(name=user_app_name, user=request.user)
    except get_application_model().DoesNotExist:
        return {'code': 'user_app/not_found', 'values': [user_app_name]}, 404, False

    return {'code': 'ok', 'data': helpers.objects_to_json(request, [item])}, 200, item


def get_list(request):
    from oauth2_provider.models import get_application_model

    try:
        items = get_application_model().objects.all()
    except:
        items = []

    return {'code': 'ok', 'data': helpers.objects_to_json(request, items)}, 200, items
