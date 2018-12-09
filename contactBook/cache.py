import hashlib
import json
from django.core.cache import cache
from .views import *
class CacheService():
    def __init__(self, view=None, **kwargs):
        self.data = kwargs
        self.data.update({'view_name': view})
        self.key = self.prepare_key()
    def prepare_key(self):
        return hashlib.md5(json.dumps(self.data, sort_keys=True).encode('utf-8')).hexdigest()
    def set_to_cache(self, qs):
        cache.set(self.key, qs)
    def unset_cache(self, qs):
        cache.set(self.key, None)
    def delete_key_value(self):
        cache.delete(self.key)
    def get_from_cache(self):
        return cache.get(self.key,None)
    def clear_all_cache(self):
        cache.clear()