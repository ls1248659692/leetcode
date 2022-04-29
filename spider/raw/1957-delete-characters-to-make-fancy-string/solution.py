class Solution:
    def makeFancyString(self, s: str) -> str:
        def dsplit(s):
            r = [s[0]]
            for c in s[1:]:
                if c != r[-1][-1]:
                    r.append(c)
                else:
                    r[-1] += c
            return r
        rli = dsplit(s)
        return ''.join([rr[:2] for rr in rli])