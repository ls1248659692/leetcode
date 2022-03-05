class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        def v1(s):
            r = []
            ln = len(s)
            for i in range(ln):
                for j in range(i+1,ln):
                    if s[j]!=s[i]:
                        if 2*j-i<=ln and s[j:j+(j-i)] == ('1' if s[i]=='0' else '0')*(j-i):
                            r.append(s[i:2*j-i])
                        break
            #print(r)
            return len(r)

        def v2(s):
            r = 0
            ln = len(s)
            for i in range(ln):
                tk= '1' if s[i]=='0' else '0'
                for j in range(i+1,(ln+i)//2+1):
                    if s[j]!=s[i]:
                        match= True
                        for k in range(j,j+(j-i)):
                            if s[k]!=tk:
                                match=False
                                break
                        if match:r+=1
                        break
            return r

        def v3(s):
            def dsplit(s):
                r = [s[0]]
                for c in s[1:]:
                    if c != r[-1][-1]:
                        r.append(c)
                    else:
                        r[-1] += c
                return r      
            sls = dsplit(s)
            return sum(min(len(sls[i]),len(sls[i-1])) for i in range(1,len(sls)))
                      
         
        return v3(s)    
