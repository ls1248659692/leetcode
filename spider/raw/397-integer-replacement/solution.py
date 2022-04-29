class Solution:
    def integerReplacement(self, n: int) -> int:
        if n==1:return 0
        elif n%2==0: 
            return 1 + self.integerReplacement(n//2)
        else:
            return 2 + min(self.integerReplacement(n//2),self.integerReplacement(n//2+1))