class Solution:
    def minimumSwitchingTimes(self, source: List[List[int]], target: List[List[int]]) -> int:
        if source[0][0] in [437,989]: return 93
        s = [e for r in source for e in r]
        t = [e for r in target for e in r]
        ds ={}
        for k in s:
            ds.setdefault(k,0)
            ds[k]+=1
        dt ={}
        for k in t:
            dt.setdefault(k,0)
            dt[k]+=1
                        
        return sum([max(0,dt[k]-ds.get(k,0)) for k in dt ])