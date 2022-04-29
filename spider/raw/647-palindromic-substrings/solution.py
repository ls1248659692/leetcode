class Solution:
    def countSubstrings(self, s: str) -> int:
        cache={'':1}
        def check_echo(s):
            for ii in range(1,len(s)//2+1):
                if s[ii-1]!=s[-ii]:return False
            return True
        liec=[]

        for i in range(len(s)-1):
            for j in range(i+2,len(s)+1):
                if j-i<2 or s[i]!=s[j-1]:continue
                if s[i+1:j-1] in cache or check_echo(s[i:j]):
                    cache[s[i:j]]=1
                    liec.append(s[i:j])
        return len(liec)+len(s)
