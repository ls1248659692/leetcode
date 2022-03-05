class Solution:
    def compressString(self, S: str) -> str:
        def dsplit(s):
            rli = [[1,s[0]]]
            for c in s[1:]:
                if c== rli[-1][-1]:rli[-1][0]+=1
                else: rli.append([1,c])
            return rli

        if not S: return ''     
        sli = dsplit(S)
        return ''.join([e[1]+str(e[0]) for e in sli ]) if len(sli)*2<len(S) else S