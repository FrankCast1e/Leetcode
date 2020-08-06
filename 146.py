'''
@Date: 2020-07-31 15:28:25
@LastEditors: FrankCast1e
@LastEditTime: 2020-07-31 15:55:47
@FilePath: /LeetCode/146.py
'''
class LRUCache:

    def __init__(self, capacity: int):
        self.upper_bound = capacity
        self.storage_dict = dict()
        self.use_situa_queue = []

    def get(self, key: int) -> int:
        if key in self.storage_dict:
            if key in self.use_situa_queue:
                index = self.use_situa_queue.index(key)
                del self.use_situa_queue[index]
            self.use_situa_queue.append(key)
            
            return self.storage_dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.storage_dict and len(self.storage_dict) >= self.upper_bound:
                least_recent_used = self.use_situa_queue[0]
                del self.use_situa_queue[0]
                del self.storage_dict[least_recent_used]
        self.storage_dict[key] = value
        if key in self.use_situa_queue:
            index = self.use_situa_queue.index(key)
            del self.use_situa_queue[index]
        self.use_situa_queue.append(key)


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))

obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
