class SocialFeed:
    def __init__(self):
        self._items = []
        self._mod_count = 0
        
    def add(self, post: str):
        self._items.append(post)
        self._mod_count += 1
        
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return self.iter_forward()
    
    def iter_forward(self):
        return ForwardIterator(self)
    
    def iter_reverse(self):
        return ReverseIterator(self)
    
    def iter_filter(self, predicate):
        return FilterIterator(self, predicate)
    
    def _get_snapshot(self):
        # Fail Test
        return list(self._items), self._mod_count
    
class ForwardIterator:
    def __init__(self, collection: SocialFeed):
        self._collection = collection
        self._snapshot, self._expected_mod = collection._get_snapshot()
        self._index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._expected_mod != self._collection._mod_count:
            raise RuntimeError("Coleção ivalidado em tempo de execução")
        if self._index >= len(self._snapshot):
            raise StopIteration
        item = self._snapshot[self._index]
        self._index += 1
        return item
        
class ReverseIterator:
    def __init__(self, collection: SocialFeed):
        self._collection = collection
        self._snapshot, self._expected_mod = collection._get_snapshot()
        self._index = len(self._snapshot) -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._expected_mod != self._collection._mod_count:
            raise RuntimeError("Coleção ivalidado em tempo de execução")
        if self._index < 0:
            raise StopIteration
        item = self._snapshot[self._index]
        self._index -= 1
        return item
    
class FilterIterator:
    def __init__(self, collection: SocialFeed, predicate):
        self._collection = collection
        self._predicate = predicate
        self._snapshot, self,_expected_mod = collection._get_snapshot()
        self._index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._expected_mod != self._collection._mod_count:
            raise RuntimeError("Coleção ivalidado em tempo de execução")
            
            
        while self._index < len(self._snapshot):
            item = self._snapshot[self._index]
            self._index += 1
            if self._predicate(item):
                return item
        raise StopIteration
                
        
feed = SocialFeed()
feed.add("Post 1 - Bem-Vindo!")
feed.add("Post 2 - novidades")
feed.add("Post 3 - Alerta Fake News")
feed.add("Post 4 - Virginia news")
feed.add("Post 4 - Grr? Ainda válido?")

for each_post in feed:
    print(" ->", each_post)
    
    
print("\n\n")
    
for each_post in feed.iter_reverse():
    print(" ->", each_post)

        
        
        
        
        
        
        
        
        
        