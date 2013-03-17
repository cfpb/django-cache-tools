from datetime import datetime
from datetime import timedelta
from django.test import TestCase
from django.db.models.base import ModelBase
from cache_tools.models import KeyableModel

class KeyableModelTest(TestCase):

    def setUp(self):
        # Create a dummy model which extends the mixin
        self.model = ModelBase('__TestModel__', (KeyableModel,),
            { '__module__': KeyableModel.__module__ })

    def test_add_updated_at(self):
        fields = (field.name for field in self.model._meta.fields)
        self.assertIn('updated_at', fields)

    def test_cache_key_changes(self):
        instance = self.model()
        instance.updated_at = datetime.now() + timedelta(minutes=-1)
        cache_key = instance.cache_key
        instance.updated_at = datetime.now()
        self.assertNotEqual(cache_key, instance.cache_key)