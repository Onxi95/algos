class MyHashSet:

    def __init__(self):
        self.memory = set()
        

    def add(self, key: int) -> None:
        self.memory.add(key)
        

    def remove(self, key: int) -> None:
        if key in self.memory:
            self.memory.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.memory
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)