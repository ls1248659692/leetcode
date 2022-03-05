class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        ar = [s.count(ch) for ch in set(list(s)) if s.count(ch)%2!=0 ]
        return  len(ar)<=1 
        
        #for i in range(1,len(s)//2+1):
        #    if s[-i] !=s[i-1]: return False
        #return True