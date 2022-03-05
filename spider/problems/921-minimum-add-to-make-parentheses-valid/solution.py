class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        #this one
        def rp(s):
            n = 0
            pn = []
            for i in range(len(s)):
                c= s[i]
                if c=='(':n+=1
                pn.append(-n if s[i:i+2]==')(' or s[i-1:i+1]==')(' else n )
                if c==')':n-=1
            return pn
                    
        while '()' in s: s=s.replace('()','')
        print(s)
        return len(s)