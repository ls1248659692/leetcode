class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def cmb(n,k):
            if k==0 or len(n)==0: return [[]]
            s0= cmb(n[1:],k)
            s1= [[n[0]]+e for e in cmb(n[1:],k-1)]
            return [e for e in s0+s1 if len(e)==k]
        r= cmb([e for e in range(1,n+1)],k) 
        return [e for e in r if len(e)==k]   