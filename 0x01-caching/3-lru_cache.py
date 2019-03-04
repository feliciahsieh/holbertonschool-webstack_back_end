#!/usr/bin/python3
"""3-lru_cache.py - LRU cache """
from base_caching import *
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache class definition
    """

    def __init__(self):
        """ __init__() - LRUCache constructor
        """
        super().__init__()

    def put(self, key, item):
        """ put() - add entry to LRU cache
        Arguments:
        key: key for dictionary
        item: item to add to dictionary
        """
        if key is not None and item is not None:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                order_of_keys = self.cache_data.keys()
                self.cache_data[key] = item
                myTup = [(key, self.cache_data[key]) for key in order_of_keys]
                self.cache_data = OrderedDict(myTup)
            else:
                if key not in self.cache_data:
                    value = self.cache_data.popitem(last=False)
                    print("DISCARD: {}".format(value[0]))
                self.cache_data[key] = item
                self.cache_data.move_to_end(key)

    def get(self, key):
        """ get() - get entry from LIFO cache
        Arguments:
        key: key for dictionary
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
