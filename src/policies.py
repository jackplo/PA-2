from abc import ABC, abstractmethod
from collections import deque, OrderedDict, defaultdict

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
        self.cache = []
        self.uniques: set[int] = set()
        
    def get(self, id:int) ->bool:
        if id in self.uniques:
            self.cache.remove(id)
            self.cache.insert(0,id)
            return True
        self.misses += 1
        
        if len(self.cache) >= self.k:
            removed = self.cache.pop()
            self.uniques.remove(removed)
            
        self.cache.insert(0,id)
        self.uniques.add(id)
        return False

class OPTFFCache(BaseCache):
    
    def __init__(self, k: int, rm: list[int]):
        super().__init__(k)
        self.occurrences: dict[int, deque[int]] = defaultdict(deque) 
        for idx, r in enumerate(rm):
            self.occurrences[r].append(idx)

        self.cache: list[int] = []
        self.uniques: set[int] = set()

    def get(self, id: int) -> bool:
        self.occurrences[id].popleft()
        
        if id not in self.uniques:
            self.misses += 1
            if len(self.cache) >= self.k:
                evictee = self.cache[0] 
                evictee_next = -1
                for request in self.cache: 
                    if len(self.occurrences[request]) == 0:
                        evictee = request 
                        break
                    elif self.occurrences[request][0] > evictee_next:
                        evictee_next = self.occurrences[request][0]
                        evictee = request

                self.cache.remove(evictee)
                self.uniques.remove(evictee)

            self.cache.append(id)
            self.uniques.add(id)
            return False
        else:
            return True
