class MyLinkedList:

    def __init__(self):
        self.ls=[]


    def get(self, index: int) -> int:
        return self.ls[index] if self.ls and 0<=index<len(self.ls) else -1


    def addAtHead(self, val: int) -> None:
            self.ls.insert(0,val)
            return True
        

    def addAtTail(self, val: int) -> None:
            self.ls.append(val)
            return True

    def addAtIndex(self, index: int, val: int) -> None:
        if index<= len(self.ls):
            if index<0:index=0
            self.ls.insert(index,val)
        elif index == len(self.ls):
            self.ls.append(val)
        else:
            return

    def deleteAtIndex(self, index: int) -> None:
        if 0<=index<len(self.ls):
            self.ls.pop(index)
            return True
        else:
            return False


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)