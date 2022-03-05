class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        def v1(n,relation,k):
            def reach(path):
                seta,tset=set([n-1]),dict({n-1:[]})
                while seta:
                    for a,b in path:
                        seta_,seta = set(seta),set()
                        if b in seta_:
                            seta.add(a)
                            for p in tset[b]:
                                p.append(a)
                return tset

            tset = reach(relation)
            print(tset)
            return min(len(pa) for pa in tset if pa[0]==0)<=k

        def v2(n,relation,k):
            def reach(path):
                seta,tset=set([n-1]),set()
                cnt =0
                while seta:
                    if cnt>k:break
                    cnt+=1
                    seta_,seta = set(seta),set()
                    for a,b in path:
                        if b in seta_:
                            seta.add(a)
                            tset.add((a,'s%d'%cnt))
                return tset
            tset = reach(relation)
            print(tset)
            pli = [1 for pa in tset if pa[0]==0 and pa[1]<='s%d'%k]
            return len(pli) if pli else 0
            
        def v3(n,relation,k):
            def reach(path):
                seta,tpa=set([n-1]),set([(n-1,)])
                cnt =0
                while seta:
                    if cnt>=k:break
                    cnt+=1
                    print(seta)
                    seta_,seta = set(seta),set()
                    for a,b in path:
                        if b in seta_:
                            seta.add(a)
                            tpa_=set(tpa)
                            for p in tpa_:
                                if p[0]==b:
                                    tpa.add(tuple([a]+list(p)))
                    
                return tpa
            tpa = reach(relation)
            print(tpa)
            # pli = [pa for pa in tpa if pa[0]==0 and len(pa)==k+1]
            pli = set([tuple(pa) for pa in tpa if pa[0]==0 and len(pa)==k+1])
            return len(pli) if pli else 0      

        def v4(n,relation,k):
            def reach(path):
                seta,tpa=set([n-1]),set([(n-1,)])
                cnt =0
                while seta:
                    if cnt>=k:break
                    cnt+=1
                    print(seta)
                    seta_,seta = set(seta),set()
                    for a,b in path:
                        if b in seta_:
                            seta.add(a)
                            seta.add((a,b))
                    tpa_,tpa=set(tpa),set()
                    for e in seta:
                        if not isinstance(e,tuple):continue
                        a,b=e
                        for p in tpa_:
                            if p[0]==b:
                                tpa.add(tuple([a]+list(p)))
                    
                return tpa
            tpa = reach(relation)
            #print(tpa)
            # pli = [pa for pa in tpa if pa[0]==0 and len(pa)==k+1]
            pli = set([tuple(pa) for pa in tpa if pa[0]==0 and len(pa)==k+1])
            return len(pli) if pli else 0
        return v4(n,relation,k)    