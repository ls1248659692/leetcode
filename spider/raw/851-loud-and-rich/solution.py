class Solution:
    def loudAndRich(self, req: List[List[int]], quiet: List[int]) -> List[int]:
        d,td={},{}
        for a,b in req: d.setdefault(b,set()).add(a)
        for b in d:
            aset,tset=set(d[b]),set(d[b])
            while aset:
                _aset,aset=set(aset),set()
                for bb in _aset:
                    for aa in d.get(bb,set()):
                        if aa not in tset:aset.add(aa)
                for ba in aset:tset.add(ba)
            td[b]=set(tset)  
        r=list(range(len(quiet)))
        for b in sorted(td.keys()):
            r[b]=sorted(list(td[b].union(set([b]))),key=lambda x:quiet[x])[0]
        return r
