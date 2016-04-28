# -*- coding: utf-8 -*-
from project import helpers


def create(request):
    json_data = request.POST

    if json_data is False:
        return {'code': 'no_data'}, 404, False

    user = helpers.getUser(request)

    if not user or not request.user.is_superuser:
        return {'code': 'no_access'}, 404, False
    if user is None:
        return {'code': 'account/not_active'}, 404, False

    return {'code': 'ok'}, 200, True
