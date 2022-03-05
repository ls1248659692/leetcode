class Solution:
    def validPalindrome(self, s: str) -> bool:

        def ispl(s):
            for i in range(1,len(s)//2+1):
                if s[i-1]!=s[-i]:return False
            return True
        if ispl(s):return True

        for i in range(1,len(s)//2+1):
            if s[i-1]==s[len(s)-i]:
                pass
            else:
                return ispl(s[:i-1]+s[i:]) or ispl(s[:len(s)-i]+s[len(s)-i+1:])
                #if ispl(s[:i]+s[i+1:]):return True
        return False
