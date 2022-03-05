class Solution:
    def makeGood(self, s: str) -> str:
        upplow = lambda c1,c2:  c1!=c2 and (c1==c2.lower() or c1==c2.upper())
        chk= lambda s: [i for i in range(len(s)-1) if upplow(s[i],s[i+1])]

        t = chk(s)
        while t:
            s,t= s[:t[0]]+s[t[0]+2:],chk(s[:t[0]]+s[t[0]+2:])
        return s
