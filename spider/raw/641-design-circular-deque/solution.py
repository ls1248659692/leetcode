class MyCircularDeque:

    def __init__(self, k: int):
        self.k=k
        self.ls=[]

    def insertFront(self, value: int) -> bool:
        if len(self.ls)<self.k:
            self.ls.insert(0,value)
            return True
        else:
            # self.ls.pop(0)
            # self.ls.append(value)
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.ls)<self.k:
            self.ls.append(value)
            return True
        else:
            # self.ls.pop(0)
            # self.ls.append(value)
            return False

    def deleteFront(self) -> bool:
        if self.ls:
            self.ls.pop(0)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.ls:
            self.ls.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        return self.ls[0] if self.ls else -1

    def getRear(self) -> int:
        return self.ls[-1] if self.ls else -1

    def isEmpty(self) -> bool:
        return True if not self.ls else False

    def isFull(self) -> bool:
        return len(self.ls)==self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()