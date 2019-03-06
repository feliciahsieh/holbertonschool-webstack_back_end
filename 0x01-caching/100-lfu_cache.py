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
                self.cache_data[key] = item
                myTup = [(key, self.cache_data[key]) for key in order_of_keys]
                self.cache_data = OrderedDict(myTup)

                if key not in self.count:
                    self.count[key] = 1
                else:
                    self.count[key] += 1
            else:
                if key not in self.cache_data:
                    value = self.cache_data.popitem(last=False)
                    print("DISCARD: {}".format(value[0]))
                    for k, v in self.cache_data.items():
                        if v == value:
                            del self.count[key]
                            break

                self.cache_data[key] = item
                self.cache_data.move_to_end(key)
                if key not in self.count:
                    self.count[key] = 1
                else:
                    self.count[key] += 1

    def get(self, key):
        """ get() - get entry from LIFO cache
        Arguments:
        key: key for dictionary
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key, last=False)
        self.count[key] += 1
        return self.cache_data[key]
