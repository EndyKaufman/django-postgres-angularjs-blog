# -*- coding: utf-8 -*-

def getUserData(user):
    if not user.is_authenticated:
        return {'userId': False, 'userData': {}}

    roles = []
    if user.is_staff:
        roles.append('user')
    if user.is_superuser:
        roles.append('admin')

    return {'code': 'ok', 'data': [{
        'userId': user.id,
        'userData': {
            "username": user.username,
            "email": user.email,
            "firstname": user.first_name,
            "lastname": user.last_name,
            "roles": roles
        }}]}
