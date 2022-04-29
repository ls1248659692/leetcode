class Solution:
    def validPalindrome(self, s: str) -> bool:
        def echo(ss):
            #print(ss)
            for ii in range(1,len(ss)//2+1):
                if ss[ii-1]!=ss[-ii]:return False
            return True
        
        if echo(s):return True
        badlt=0
        for i in range(1,len(s)//2+1):
           if s[i-1]!=s[-i]:
                badlt+=1
                return  echo(s[:i-1]+s[i:]) or echo(s[:-i]+(s[-i+1:] if i>1 else ''))
        return False       