# -*- coding: utf-8 -*-

def getUserData(user):
    roles = []

    if user.is_staff:
        roles.append('user')
    if user.is_superuser:
        roles.append('admin')

    if len(roles) == 0:
        return {'userId': False, 'userData': {}}

    return {
        'userId': user.id,
        'userData': {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "firstname": user.first_name,
            "lastname": user.last_name,
            "roles": roles
        }}
