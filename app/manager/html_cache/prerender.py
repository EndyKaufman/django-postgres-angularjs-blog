from django_seo_js import settings
from django_seo_js.backends.base import SEOBackendBase
from django_seo_js.backends.prerender import PrerenderHosted
from django.http import HttpResponse
import requests
import resource


class CustomPrerenderHosted(PrerenderHosted):
    """Implements the backend for an arbitrary prerender service
       specified in settings.SEO_JS_PRERENDER_URL"""

    def get_response_for_url(self, url):
        """
        Accepts a fully-qualified url.
        Returns an HttpResponse, passing through all headers and the status code.
        """

        if not url or "//" not in url:
            raise ValueError("Missing or invalid url: %s" % url)

        if url != '':
            render_url = self.BASE_URL + url.rstrip('/')
        else:
            render_url = self.BASE_URL.rstrip('/')

        headers = {
            'X-Prerender-Token': self.token,
        }
        get_options = {
            'headers': headers,
            'allow_redirects': False
        }

        item = resource.get_item_by_url(render_url)

        if not item:
            try:
                r = self.session.get(render_url, **self._request_kwargs(get_options))
                assert r.status_code < 500
                new_response = self.build_django_response_from_requests_response(r)
                resource.update_by_url(render_url, new_response.content)
                return new_response
            except requests.exceptions.Timeout:
                return self.build_request_timeout_response()

        if item.content is not None:
            r = HttpResponse(item.content)
            r['content-length'] = len(item.content)
            r.status_code = 200
            new_response = self.build_django_response_from_requests_response(r)
            return new_response
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
                resource.update_by_url(render_url, new_response.content)
                return new_response
            except requests.exceptions.Timeout:
                return self.build_request_timeout_response()
