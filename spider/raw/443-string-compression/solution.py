class Solution:
    def compress(self, chars: List[str]) -> int:
        def dsplit(s):
            rli = [[1,s[0]]]
            for c in s[1:]:
                if c== rli[-1][-1]:rli[-1][0]+=1
                else: rli.append([1,c])
            return rli

        ss = ''.join(chars)
        if not ss: return ''     
        sli = dsplit(ss)
        slib= [e[1]+ (str(e[0]) if e[0]>1 else '') for e in sli ]
        print(slib)
        slic= list(''.join(slib))
        for i in range(len(slic)):
            chars[i]=slic[i]
        return len(slic)