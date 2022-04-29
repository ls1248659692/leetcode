class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d ={}
        for n in arr1:
            d.setdefault(n,0)
            d[n]+=1
        r =[]
        for n in arr2:
            for j in range(d[n]):
                r.append(n)
        db = [e for e in d.items() if e[0] not in arr2]
        srt = sorted(db,key=lambda xx:xx[0])
        for k,v in srt:
            for j in range(v):
                r.append(k)
        return r