class MyCircularQueue:

    def __init__(self, k: int):
        self.k=k
        self.ls=[]


    def enQueue(self, value: int) -> bool:
        if len(self.ls)<self.k:
            self.ls.append(value)
            return True
        else:
            # self.ls.pop(0)
            # self.ls.append(value)
            return False
        

    def deQueue(self) -> bool:
        if self.ls:
            self.ls.pop(0)
            return True
        else:
            return False


    def Front(self) -> int:
        return self.ls[0] if self.ls else -1


    def Rear(self) -> int:
        return self.ls[-1] if self.ls else -1


    def isEmpty(self) -> bool:
        return True if not self.ls else False


    def isFull(self) -> bool:
        return len(self.ls)==self.k



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()