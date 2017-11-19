from collections import deque

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.keys = deque()
        self.cache = {}
        self.maxsize = capacity
        self.length = 0

    def get(self, key):
        """
        O(n) complexity
        :type key: int
        :rtype: int
        """

        if key not in self.cache:
            return -1
        self.update(key)
        return self.cache[key]

    def update(self, key):
        """
        O(n) key
        :param key:
        :return:
        """
        self.keys.remove(key)
        self.keys.append(key)

    def put(self, key, val):
        """
        O(n) complexity
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache[key] = val
            self.update(key)
            return
        if self.length == self.maxsize:
            k = self.keys.popleft()
            del self.cache[k]
            self.length -= 1
        self.keys.append(key)
        self.cache[key] = val
        self.length += 1
        return



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)