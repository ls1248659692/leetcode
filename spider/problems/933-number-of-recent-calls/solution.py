class RecentCounter:

    def __init__(self):
        self.cnt =0
        self.que =[]

    def ping(self, t: int) -> int:
        self.que.append(t)
        while self.que[0]<t-3000:self.que.pop(0)
        return len(self.que)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)