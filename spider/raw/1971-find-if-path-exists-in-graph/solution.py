class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        seg0 = [[e[1],e[0]] for e in edges]+edges
        dicb,dice={},{}
        for b,e in seg0:
            dicb.setdefault(b,set())
            dicb[b].add(e)
        for b,e in seg0:
            dice.setdefault(e,set())
            dice[e].add(b) 

        rset = set([destination])
        cnt =1
        while cnt<n and source not in rset:
            cnt+=1
            if cnt%100==1: print(cnt,len(rset))
            t0 = list()
            for e in rset:
                t0.append(dice[e])
            rset = set([e for t in t0 for e in t])
        return source in rset
