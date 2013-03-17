from functools import wraps
from django.core.cache import cache
from django.http import HttpRequest
from django.utils.cache import get_cache_key
from django.views.decorators.cache import cache_page
from django.utils.decorators import available_attrs

TIME_TO_CACHE = 172800 # 2 days * 24 hours * 60 minutes * 60 seconds = 172800

def expire_page(path):
    request = HttpRequest()
    request.path = path
    key = get_cache_key(request)
    if key and cache.has_key(key):
        cache.delete(key)

def cache_page_in_group(group):
    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            key_prefix = get_group_key(group)
            return cache_page(TIME_TO_CACHE, key_prefix=key_prefix)(view_func)(request, *args, **kwargs)
        return _wrapped_view
    return decorator

def get_group_key(group):
    key = cache.get("cache_group_" + str(group), 1)
    return str(group) + str(key)

def expire_cache_group(group):
    group_key = "cache_group_" + str(group)
    value = int(cache.get(group_key, 1)) + 1
    cache.set(group_key, value, TIME_TO_CACHE)
    return value
