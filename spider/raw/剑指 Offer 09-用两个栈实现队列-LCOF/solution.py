class CQueue:

    def __init__(self):
        self.st1 =[]
        self.st2= []


    def appendTail(self, value: int) -> None:
        self.st1.append(value)


    def deleteHead(self) -> int:
        while self.st1: self.st2.append(self.st1.pop())
        val = self.st2.pop() if self.st2 else -1
        while self.st2: self.st1.append(self.st2.pop())
        return val
