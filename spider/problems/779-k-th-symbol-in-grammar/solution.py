class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:return 0
        r = 2**(n-1)
        if k % 2:
            return self.kthGrammar(n-1,(k+1)/2)
        else:
            return abs(self.kthGrammar(n-1,k/2)-1)