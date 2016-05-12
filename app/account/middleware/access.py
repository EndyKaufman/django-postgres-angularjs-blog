from django.middleware.csrf import CsrfViewMiddleware


class AccessViewMiddleware(CsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        import json
        try:
            token = request.POST['token']
            token_from_post = True
        except:
            token_from_post = False

        try:
            data = json.loads(request.body)
        except:
            data = False

        if data:
            try:
                token = data['token']
                token_from_payload = True
            except:
                token_from_payload = False
        else:
            token_from_payload = False

        if token_from_post or token_from_payload:
            setattr(request, '_dont_enforce_csrf_checks', True)

            setattr(request, 'TOKEN', token)

            if token_from_post:
                setattr(request, 'DATA', request.POST)

            if token_from_payload:
                setattr(request, 'DATA', data)
        else:
            setattr(request, 'TOKEN', False)
            setattr(request, 'DATA', data)

        retval = super(AccessViewMiddleware, self).process_view(request, callback, callback_args, callback_kwargs)

        return retval
