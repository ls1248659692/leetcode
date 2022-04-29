class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        d,td={},{}
        for i,e in enumerate(graph): d.setdefault(i,set(list(e)))
        it = sorted(d.items(),key=lambda x:len(x[1]),reverse=True)
        print(it)
        p0,p1,new,sing,cnt=[],[],[],[],0
        for b,s in it:
            aset,tset=set([b]),set([b])
            if not p0+p1: p0.append(b)
            if b in p0 and b in p1:return False
            elif b in p1: cnt=1
            elif b in p0: cnt=0
            else: 
                if s:
                    new.append(set([b])|s)
                    print('new point',b)
                else:
                    sing.append(b)
                continue
            while aset:
                _aset,aset,cnt=set(aset),set(),cnt+1
                for bb in _aset:
                    for aa in d.get(bb,set()):
                        if aa not in tset:
                            aset.add(aa)
                            p1.append(aa) if cnt%2 else p0.append(aa)
                for ba in aset:tset.add(ba)
            td[b]=set(tset) |set([b])
        if new:
            pn=set()
            for s in new: pn|=s
            return not(pn & set(p0+p1))
            print(p)
        return  len(set(p1+p0+sing))==len(graph)