class MinStack:

    def __init__(self):
        self.li=[]

    def push(self, val: int) -> None:
        self.li.append(val)


    def pop(self) -> None:
        self.li.pop()

    def top(self) -> int:
        return self.li[-1]


    def min(self) -> int:
        return min(self.li) if self.li else None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()