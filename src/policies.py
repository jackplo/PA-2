from abc import ABC, abstractmethod
from collections import deque, OrderedDict

class BaseCache(ABC):

    def __init__(self, k: int):
        self.k = k
        self.misses = 0

    @abstractmethod
    def get(self, id: int) -> bool:
        pass

    def get_miss_count(self) -> int:
        return self.misses
    
class FIFOCache(BaseCache):

    def __init__(self, k: int):
        super().__init__(k)
        self.cache: deque[int] = deque()
        self.uniques: set[int] = set()

    def get(self, id: int) -> bool:
        if id not in self.uniques:
            self.misses += 1
            if len(self.cache) >= self.k:
                evictee = self.cache.popleft()
                self.uniques.remove(evictee)
           
            self.cache.append(id)
            self.uniques.add(id)
            return False
        else:
            return True
        
        
class LRUCache(BaseCache):
    def  __init__(self, k:int):
        super().__init__(k)
        self.cache = OrderedDict()
        
    def get(self, id:int) ->bool:
        #if id in cache, move to end (most recent)
        if id in self.cache:
            self.cache.move_to_end(id)
            return True
        self.misses +=1
        
        #if cache is at max capacity, removes least recent used (at front) 
        if len(self.cache) >= self.k:
            self.cache.popitem(last = False)
        
        self.cache[id] = None
        return False