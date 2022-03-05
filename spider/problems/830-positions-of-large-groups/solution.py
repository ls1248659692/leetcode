class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        def dsplit(s):
            r = [s[0]]
            for c in s[1:]:
                if c == r[-1][-1]:
                    r[-1] += c
                else:
                    r.append(c)
            return r
        sli = dsplit(s)        
        nli = [len(s) for s in sli]
        c=0
        res = []
        for n in nli:
            if n>=3: res.append([c,c+n-1])
            c+=n
        return res