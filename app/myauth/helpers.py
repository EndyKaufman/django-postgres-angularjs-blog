# -*- coding: utf-8 -*-

def getUserData(user):
    #from django.contrib.auth.models import User

    #user = User.objects.get(id=user.id)

    roles = []

    if user.is_staff:
        roles.append('user')
    if user.is_superuser:
        roles.append('admin')

    if len(roles) == 0:
        return {}

    return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "firstname": user.first_name,
            "lastname": user.last_name,
            "roles": roles
        }
