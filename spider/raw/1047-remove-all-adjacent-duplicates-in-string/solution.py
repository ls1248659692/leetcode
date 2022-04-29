def dupa(s,b):
    for i in range(b+1,len(s)):
        b,e,m = i-1,i,False
        while b>=0 and e<len(s) and s[b]==s[e]:
            b-=1
            e+=1
            m=True
        if m: return b+1,e-1
    return -1,-1  

class Solution:
    def removeDuplicates(self, s: str) -> str:
        b,e =   dupa(s,0)    
        while b>=0: 
            s= s[:b]+s[e+1:]
            b,e =   dupa(s,b)
        return s