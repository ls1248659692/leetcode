class Solution:
    def canFinish(self, num: int, req: List[List[int]]) -> bool:
        d={}
        for b,a in req:
            d.setdefault(b,set()).add(a)
            #d[b].add(a)
        print(d)
        for b in d:
            aset,tset=set(d[b]),set(d[b])
            print('tset_begin',b,tset)
            while aset:
                _aset,aset=set(aset),set()
                for bb in _aset:
                    for a in d.get(bb,set()):
                        if a not in tset:aset.add(a)
                for e in aset:tset.add(e)
            print('tset_end',b,tset)
            if b in tset:return False
        return True