from django_seo_js import settings
from django_seo_js.backends.base import SEOBackendBase
from django_seo_js.backends.prerender import PrerenderIO
import requests

class PrerenderHosted(PrerenderIO):
    """Implements the backend for an arbitrary prerender service
       specified in settings.SEO_JS_PRERENDER_URL"""

    def __init__(self, *args, **kwargs):
        super(SEOBackendBase, self).__init__(*args, **kwargs)
        self.token = ""
        if not settings.PRERENDER_URL:
            raise ValueError("Missing SEO_JS_PRERENDER_URL in settings.")
        if not settings.PRERENDER_RECACHE_URL:
            raise ValueError("Missing SEO_JS_PRERENDER_RECACHE_URL in settings.")

        self.BASE_URL = settings.PRERENDER_URL
        self.RECACHE_URL = settings.PRERENDER_RECACHE_URL

    def _get_token(self):
        pass

    def update_url(self, url=None):
        """
        Accepts a fully-qualified url.
        Returns True if successful, False if not successful.
        """
        if not url:
            raise ValueError("Neither a url or regex was provided to update_url.")
        post_url = "%s%s" % (self.BASE_URL, url)
        r = self.session.post(post_url)
        return int(r.status_code) < 500