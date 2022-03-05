class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dic= {}
        for b,a in edges:
            dic.setdefault(b,[]).append(a)
            dic.setdefault(a,[]).append(b)
        td={}
        for b in dic:
            aset,tset =set(dic[b]),set(dic[b])
            while aset:
                _aset,aset=set(aset),set()
                for bb in _aset:
                    for aa in dic.get(bb,set()):
                        if aa not in tset:
                            aset.add(aa)
                for p in aset:tset.add(p)
            td[b]=tset |set([b])
        for i in range(n):
            td.setdefault(i,set([i]))
        #print(td)
        return len(set([tuple(e) for e in td.values()]))
