class Solution:
    def checkIfPrerequisite(self, num: int, req: List[List[int]], qy: List[List[int]]) -> List[bool]:
        d={}
        for a,b in req:
            d.setdefault(b,set())
            d[b].add(a)
        print(d)
        td={}
        for b in d:
            aset,tset=set(d[b]),set(d[b])
            #print('tset_begin',b,tset)
            while aset:
                _aset,aset=set(aset),set()
                for bb in _aset:
                    for a in d.get(bb,set()):
                        if a not in tset:aset.add(a)
                for e in aset:tset.add(e)
            #print('tset_end',b,tset)
            td[b]=set(tset)
            if b in tset:return []
        print(td)
        if not td: return [False for _ in range(num)]
        return [a in td.get(b,set()) for a,b in qy]             