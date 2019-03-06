#!/usr/bin/python3
"""100-lfu_cache.py - LFU cache - Least Frequently Used """
from base_caching import *
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache class definition
    """

    def __init__(self):
        """ __init__() - LFUCache constructor
        """
        self.count = {}
        super().__init__()

    def put(self, key, item):
        """ put() - add entry to LFU cache
        Arguments:
        key: key for dictionary
        item: item to add to dictionary
        """
        if key is not None and item is not None:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                order_of_keys = self.cache_data.keys()
                order_of_keys_c = self.count.keys()
                if key in self.cache_data:
                    self.cache_data[key] = item
                    self.count[key] += 1
                else:
                    self.cache_data[key] = item
                    self.count[key] = 1

                myTup = [(key, self.cache_data[key]) for key in order_of_keys]
                self.cache_data = OrderedDict(myTup)

                CntTup = [(key, self.count[key]) for key in order_of_keys_c]
                self.count = OrderedDict(CntTup)
            else:
                if key not in self.cache_data:
                    minKey = min(self.count, key=self.count.get)
                    del self.cache_data[minKey]
                    print("DISCARD: {}".format(minKey))
                    del self.count[minKey]
                    self.cache_data[key] = item
                    self.count[key] = 1
                else:
                    self.cache_data[key] = item
                    self.count[key] += 1

    def get(self, key):
        """ get() - get entry from LIFO cache
        Arguments:
        key: key for dictionary
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key, last=True)
        self.count[key] += 1
        self.count.move_to_end(key, last=True)
        return self.cache_data[key]
