from queue import Queue
class MyStack:

    def __init__(self):
        self.q0 = Queue()
        self.q1 = Queue()

    def push(self, x: int) -> None:
        self.q0.put(x)
        #print(self.q0.qsize())

    def pop(self) -> int:
        while self.q0.qsize()>1:
            self.q1.put(self.q0.get())
        r = self.q0.get()
        while self.q1.qsize()>0:
            self.q0.put(self.q1.get())
        return r

    def top(self) -> int:
        while self.q0.qsize()>1: self.q1.put(self.q0.get())
        t = self.q0.get()
        self.q1.put(t)
        while self.q1.qsize()>0: self.q0.put(self.q1.get())
        return t

    def empty(self) -> bool:
        return self.q0.qsize()==0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()