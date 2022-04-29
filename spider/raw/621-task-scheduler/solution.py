class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        lstcnt = [tasks.count(i) for i in set(tasks)]
        #tmax = max(lstcnt)
        return max((max(lstcnt)-1)*(n+1)+lstcnt.count(max(lstcnt)),len(tasks))
        