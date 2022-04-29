class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        #knli = sorted([candyType.count(kn) for kn in set(candyType)],reverse=False)
        dc = {}
        for c in candyType:
            dc.setdefault(c,0)
            dc[c]+=1
        knli= list(dc.keys())
        print(knli)

        return  len(knli[:len(candyType)//2])