class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        def dsplit(s):
            r=[s[0]]
            for c in s[1:]:
                if c== r[-1][-1]:r[-1] += c
                else: r.append(c)
            return r
        ds = dsplit(s)
        print(ds)
        if not s:return False
        if s=='1':return True
        return len([ss for ss in ds if '1' in ss])==1
