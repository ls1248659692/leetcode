class Solution:
    def findAllRecipes(self, rec: List[str], ig: List[List[str]], sup: List[str]) -> List[str]:
        ig,sup=[(rec[i],set(e)) for i,e in enumerate(ig)],set(sup)
        addr=[rec for rec,ing in ig if ing.issubset(sup)]
        tset,aset=set(addr),set(addr)
        while aset:
            _aset,aset=set(aset),set()
            for r in _aset:sup.add(r)
            aset= set([rec for rec,ing in ig if ing.issubset(sup) and rec not in tset])
            for p in aset:tset.add(p)
        return list(tset)
            