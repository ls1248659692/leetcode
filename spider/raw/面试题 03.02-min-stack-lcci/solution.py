class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.li=[]

    def push(self, x: int) -> None:
        self.li.append(x)


    def pop(self) -> None:
        self.li.pop()


    def top(self) -> int:
        return self.li[-1]


    def getMin(self) -> int:
        return min(self.li)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()