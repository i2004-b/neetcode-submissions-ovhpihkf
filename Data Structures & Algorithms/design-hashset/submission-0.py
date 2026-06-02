class MyHashSet:

    def __init__(self):
        # Initialize with hashtable
        self.table = {}

    def add(self, key: int) -> None:
        if not key in self.table:
            self.table[key] = 1

    def remove(self, key: int) -> None:
        if key in self.table:
            del self.table[key]

    def contains(self, key: int) -> bool:
        return True if key in self.table else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)