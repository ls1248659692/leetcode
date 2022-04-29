class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        dl = {'r':{},'c':{},'x':{},'y':{}}
        def rcxy():
            for r,c in lamps:
                for k,sk in [('r',r),('c',c),('x',r-c),('y',r+c)]:
                    dl[k].setdefault(sk,set())
                    dl[k][sk].add((r,c))

        def isbr(r,c):
            ans =r in dl['r'] or c in dl['c'] or r-c in dl['x'] or r+c in dl['y']
            for rr in [r-1,r,r+1]:
                for cc in [c-1,c,c+1]:
                    for k,sk in [('r',rr),('c',cc),('x',rr-cc),('y',rr+cc)]:
                        # print(k,sk,rr,cc,r,c)
                        if sk in dl[k]: 
                            # print('dl',k,sk,rr,cc)
                            dl[k][sk].discard((rr,cc))
                            if not dl[k][sk]:del dl[k][sk]
            #print(dl)
            return 1 if ans else 0
        rcxy()
        #print(dl)
        return [isbr(q[0],q[1]) for q in queries]