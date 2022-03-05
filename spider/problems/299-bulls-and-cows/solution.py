class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s,g,ln=secret,guess,len(secret)
        hits = [i for i in range(ln)if s[i]==g[i]]
        exh_s = [s[i] for i in range(ln)if s[i]!=g[i]]
        
        phits = [g[i] for i in range(ln) if s[i]!=g[i] and g[i] in exh_s and i not in hits ]
        phits_1 = [min(phits.count(co),s.count(co)) for co in set(phits)]
        phits_1 = [min(phits.count(co),exh_s.count(co)) for co in set(phits)]
        print(hits,phits,phits_1)
        return '%dA%dB'%(len(hits),sum([e for e in phits_1]))      