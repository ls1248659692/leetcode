class Solution:
    def canCompleteCircuit(self, g: List[int], c: List[int]) -> int:
        d=[g[i]-c[i] for i in range(len(g))]
        cd=list(d)
        for i in range(1,len(d)):cd[i] += cd[i-1]
        mi=min(cd)
        if mi >0 or(mi==0 and len(g)-1== cd.index(mi)):return 0
        ncd = [e-mi for e in cd]
        midx= cd.index(mi)
        ncd[midx]=float('inf')
        print(d,'
',cd,'
',ncd,'
',)
        return cd.index(mi)+1 if min(ncd)>0 and cd[-1]>=0 else -1
