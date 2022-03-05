class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        r=''.join([s[n-k:n][::-1] + s[n:n+k] for n in range(k,len(s)+k,2*k)])
        print(r)
        return s if k==1 else r if k<len(s) else s[::-1]