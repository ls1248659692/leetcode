class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck)==1: return False
        ct=[deck.count(n) for n in set(deck)]
        print(ct)
        sc = set(ct)
        mi = min(ct)
        if ct==1:return False
        for mmi in range(2,mi+1):
            if sum(c%mmi for c in ct)==0:return True
        return False