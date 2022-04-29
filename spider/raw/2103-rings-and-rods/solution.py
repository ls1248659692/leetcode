class Solution:
    def countPoints(self, rings: str) -> int:
        ts = ''.join(list(set([rings[i:i+2] for i in range(0,len(rings),2)])))
        print(ts)
        return len([i for i in range(10) if ts.count(str(i))==3])
