class MyHashSet:

    def __init__(self):
        self.ts=set()

    def add(self, key: int) -> None:
        self.ts.add(key)


    def remove(self, key: int) -> None:
         self.ts.discard(key)


    def contains(self, key: int) -> bool:
        return  key in self.ts



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)