from django_seo_js import settings
from django_seo_js.backends.base import SEOBackendBase
from django_seo_js.backends.prerender import PrerenderIO
from django.http import HttpResponse
import requests
import resource


class CustomPrerenderIO(PrerenderIO):
    """Implements the backend for an arbitrary prerender service
       specified in settings.SEO_JS_PRERENDER_URL"""

    def __init__(self, *args, **kwargs):
        super(SEOBackendBase, self).__init__(*args, **kwargs)
        self.token = self._get_token()

        if not settings.PRERENDER_URL:
            raise ValueError("Missing SEO_JS_PRERENDER_URL in settings.")
        if not settings.PRERENDER_RECACHE_URL:
            raise ValueError("Missing SEO_JS_PRERENDER_RECACHE_URL in settings.")

        self.BASE_URL = settings.PRERENDER_URL
        self.RECACHE_URL = settings.PRERENDER_RECACHE_URL

    def update_url(self, url=None, regex=None):
        """
        Accepts a fully-qualified url, or regex.
        Returns True if successful, False if not successful.
        """

        if not url and not regex:
            raise ValueError("Neither a url or regex was provided to update_url.")

        headers = {
            'X-Prerender-Token': self.token,
            'Content-Type': 'application/json',
        }
        data = {
            'prerenderToken': settings.PRERENDER_TOKEN,
        }
        if url:
            data["url"] = url
        if regex:
            data["regex"] = regex

        r = self.session.post(self.RECACHE_URL, headers=headers, data=data)
        return r.status_code < 500

    def _request_kwargs(self, kwargs):
        if settings.PRERENDER_TIMEOUT is not False:
            kwargs['timeout'] = settings.PRERENDER_TIMEOUT
        return kwargs

    def get_response_for_url(self, url):
        """
        Accepts a fully-qualified url.
        Returns an HttpResponse, passing through all headers and the status code.
        """
        if not url or "//" not in url:
            raise ValueError("Missing or invalid url: %s" % url)

        new_url = url.replace('?_escaped_fragment_=', '')
        new_url = new_url.replace('_escaped_fragment_=', '')

        if new_url != '':
            new_url = new_url.rstrip('/')

        render_url = self.BASE_URL + new_url

        headers = {
            'X-Prerender-Token': self.token
        }

        get_options = {
            'headers': headers,
            'allow_redirects': False
        }

        item = resource.get_item_by_url_base(new_url)

        if not item:
            try:
                r = self.session.get(render_url, **self._request_kwargs(get_options))
                assert r.status_code < 500
                new_response = self.build_django_response_from_requests_response(r)
                resource.update_by_url(new_url, new_response.content)
                return new_response
            except requests.exceptions.Timeout:
                return self.build_request_timeout_response()

        if item.content is not None:
            content = item.content
            if content != '':
                content = content.replace('<meta name="fragment" content="!">', '')
            return HttpResponse(content)
        else:
            try:
                headers = {
                    'X-Prerender-Token': self.token,
                    'Content-Type': 'application/json',
                }
                data = {
                    'prerenderToken': settings.PRERENDER_TOKEN,
                }
                if url:
                    data["url"] = url

                r = self.session.post(self.RECACHE_URL, headers=headers, data=data)

                new_response = self.build_django_response_from_requests_response(r)
                resource.update_by_url(new_url, new_response.content)
                return new_response
            except requests.exceptions.Timeout:
                return self.build_request_timeout_response()
