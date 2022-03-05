class Solution:
    def generateTheString(self, n: int) -> str:
        return 'a' if n==1 else 'a'+'b'*(n-1) if n%2==0 else 'ab'+'c'*(n-2)