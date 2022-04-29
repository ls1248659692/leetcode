class Solution:
    def numberOfMatches(self, n: int) -> int:
        cnt=0
        while n>1:
            cnt += n/2 if n%2==0 else (n-1)/2
            n=  n/2 if n%2==0 else (n+1)/2
        return int(cnt)