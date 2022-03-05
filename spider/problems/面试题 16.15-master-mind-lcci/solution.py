class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        s,g=solution,guess
        hits = [i for i in range(4)if s[i]==g[i]]
        exh_s = [s[i] for i in range(4)if s[i]!=g[i]]
        
        phits = [g[i] for i in range(4) if s[i]!=g[i] and g[i] in exh_s and i not in hits ]
        phits_1 = [min(phits.count(co),s.count(co)) for co in set(phits)]
        print(hits,phits,phits_1)
        return[len(hits),sum([e for e in phits_1])]