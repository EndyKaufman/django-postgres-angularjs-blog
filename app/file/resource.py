# -*- coding: utf-8 -*-
from project import helpers


def create(request):
    json_data = request.POST

    user = helpers.getUser(request)

    json_data = helpers.setNullValuesIfNotExist(json_data, ['comment'])

    if request.FILES and request.FILES.get('file'):
        if user.is_superuser:
            url = helpers.saveFile(False,
                                   request.FILES.get('file'))
        else:
            url = helpers.saveFile(str(user.id),
                                   request.FILES.get('file'))
    else:
        url = ''

    from app.file.models import File

    file, created = File.objects.get_or_create(src=url)
    if created:
        file.comment = json_data['comment']
        file.created_user = user
        file.save()

    return file
