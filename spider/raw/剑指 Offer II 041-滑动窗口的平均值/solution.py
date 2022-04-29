class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.nli = []

    def next(self, val: int) -> float:
        if len(self.nli)>=self.size: self.nli.pop(0)
        self.nli.append(val)
        return sum(self.nli)/len(self.nli)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)