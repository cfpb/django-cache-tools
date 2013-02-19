from django.test import TestCase
from mock import Mock, MagicMock, patch
from django.test.client import RequestFactory
from cache_tools.tools import cache_page_in_group, get_group_key, expire_cache_group, TIME_TO_CACHE

class CachingTest(TestCase):
    def test_get_group_key(self):
        key = get_group_key('test')
        assert key == 'test2'

    @patch('cache_tools.tools.cache.get')
    def test_get_group_key(self, cache_get):
        cache_get.return_value = 15
        key = get_group_key('test')
        assert key == 'test15'

    @patch('cache_tools.tools.cache.get')
    @patch('cache_tools.tools.cache.set')
    def test_expire_cache_group(self, cache_set, cache_get):
        cache_get.return_value = 15
        expire_cache_group('test')
        cache_set.assert_called_with('cache_group_test', 16, TIME_TO_CACHE)


    @patch('cache_tools.tools.cache.get')
    @patch('cache_tools.tools.cache_page')
    def test_cache_group(self, cache_page, cache_get):
        cache_get.return_value = 15
        view = Mock()
        decorated_view = cache_page_in_group('test')(view)
        request = RequestFactory().get('/test/')
        response = decorated_view(request)

        cache_page.assert_called_with(TIME_TO_CACHE, key_prefix='test15')

    @patch('cache_tools.tools.cache_page')
    def test_cache_group_initial(self, cache_page):
        view = Mock()
        decorated_view = cache_page_in_group('test')(view)
        request = RequestFactory().get('/test/')
        response = decorated_view(request)

        cache_page.assert_called_with(TIME_TO_CACHE, key_prefix='test1')