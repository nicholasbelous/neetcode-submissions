class MyHashMap:

    def __init__(self):
        # Store pairs as [key, value] inside the list
        self.hash_map = [] 

    def put(self, key: int, value: int) -> None:
        # Loop through to find if the key already exists
        for pair in self.hash_map:
            if pair[0] == key:
                pair[1] = value
                return
        # If it doesn't exist, append a new pair
        self.hash_map.append([key, value])

    def get(self, key: int) -> int:
        # Search specifically for the key at index 0 of each pair
        for pair in self.hash_map:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        # Find the pair and remove it entirely
        for i, pair in enumerate(self.hash_map):
            if pair[0] == key:
                self.hash_map.pop(i)
                return
