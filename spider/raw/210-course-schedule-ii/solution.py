class Solution:
    def findOrder(self, num: int, req: List[List[int]]) -> List[int]:
        d={}
        for b,a in req:
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
        r=[]
        print(td)
        if not td: return list(range(num))
        for b,tset in sorted(td.items(),key=lambda x:len(x[1])):
            r.append(b)
            for a in tset: 
                if a not in td and a not in r: r.insert(0,a)
        for i in range(num):
            if i not in r: r.insert(0,i)
        return r
            
            
            