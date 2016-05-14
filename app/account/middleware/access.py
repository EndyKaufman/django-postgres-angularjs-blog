from django.contrib import auth
from django.middleware.csrf import CsrfViewMiddleware
from oauth2_provider.oauth2_backends import get_oauthlib_core
from oauth2_provider.backends import OAuth2Backend


class AccessViewMiddleware(CsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        import json

        try:
            data = json.loads(request.body)
        except:
            data = request.POST

        setattr(request, 'DATA', data)

        backend = OAuth2Backend()
        credentials = {'request': request}
        user = backend.authenticate(**credentials)
        if user is not None:
            user = backend.get_user(user.pk)
            request.user = user
            if user.is_active:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                auth.login(request, user)
                setattr(request, '_dont_enforce_csrf_checks', True)

        retval = super(AccessViewMiddleware, self).process_view(request, callback, callback_args, callback_kwargs)

        return retval
