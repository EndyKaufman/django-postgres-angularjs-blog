from django.utils.decorators import available_attrs, decorator_from_middleware
from app.account.middleware.access import AccessViewMiddleware
from functools import wraps

csrf_or_api_token_protect = decorator_from_middleware(AccessViewMiddleware)
csrf_or_api_token_protect.__name__ = 'csrf_or_api_token_protect'
csrf_or_api_token_protect.__doc__ = """
Use this decorator to ensure that a view sets a CSRF cookie, whether or not it
uses the csrf_token template tag, or the CsrfViewMiddleware is used.
"""


def csrf_exempt(view_func):
    """
    Marks a view function as being exempt from the CSRF view protection.
    """

    # We could just do view_func.csrf_exempt = True, but decorators
    # are nicer if they don't have side-effects, so we return a new
    # function.
    def wrapped_view(*args, **kwargs):
        return view_func(*args, **kwargs)

    wrapped_view.csrf_exempt = True
    return wraps(view_func, assigned=available_attrs(view_func))(wrapped_view)
