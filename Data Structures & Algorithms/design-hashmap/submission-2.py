class MyHashMap:

    def __init__(self):
        self.hash_map = []

    def put(self, key: int, value: int) -> None:
        if(key in self.hash_map):
            self.hash_map[self.hash_map.index(key)] = value
        else:
            self.hash_map.append(key)
            self.hash_map.append(value)
        
        return None

    def get(self, key: int) -> int:
        if key in self.hash_map:
            return self.hash_map[self.hash_map.index(key)]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        if key in self.hash_map:
            key_index = self.hash_map.index(key)
            self.hash_map.pop(key_index)
            self.hash_map.pop(key_index)
        
        return None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)