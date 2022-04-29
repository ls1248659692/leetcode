class MyQueue:

    def __init__(self):
        self.lia=[]
        self.lib=[]


    def push(self, x: int) -> None:
        self.lia.append(x)


    def pop(self) -> int:
        if not self.lia:return None
        while self.lia: self.lib.append(self.lia.pop())
        val = self.lib.pop()
        while self.lib: self.lia.append(self.lib.pop())
        return val


    def peek(self) -> int:
        if not self.lia:return None
        while self.lia: self.lib.append(self.lia.pop())
        val = self.lib.pop()
        self.lia.append(val)
        while self.lib: self.lia.append(self.lib.pop())
        return val

    def empty(self) -> bool:
        return True if not self.lia else False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()