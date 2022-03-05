class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cd = sorted(cards,reverse=True)
        n =cnt
        cda =[ c for c in cd[:n] if c%2==0]
        cdb =[ c for c in cd[:n] if c%2==1]
        su = sum(cd[:n])
        if su%2==0: return su
        na = [ c for c in cd[n:] if c%2==0]
        nb = [ c for c in cd[n:] if c%2==1]
        sua,sub = 0,0
        if (cda and  nb):
            sua= su- cda[-1]+nb[0]
        if  (cdb and  na):
            sub = su -cdb[-1]+na[0]
        return max(sua,sub)
