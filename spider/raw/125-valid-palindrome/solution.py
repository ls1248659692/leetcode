class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        sli = [ch for ch in s if 0<=ord(ch)-ord('a')<26 or ch in '01234567789']
        s = ''.join(sli)
        #print(s)
        #if len(s)==1:return False
        #for ch in ''_#@.,: ': s=s.replace(ch,'')
        for i in range(1,len(s)//2+1):
            if s[i-1]!=s[-i]:return False
        return True
        