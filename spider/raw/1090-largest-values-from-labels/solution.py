class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        setsize,scorenum,d = 0,0,{}
        for v, l in sorted([[values[i], labels[i]] for i in range(len(values))], reverse = True):
            d[l] = d.get(l, 0) + 1
            if d[l] <= useLimit:
                scorenum,setsize= scorenum+v,setsize+1
            if setsize == numWanted:
                return scorenum
        return scorenum