class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        sn = sorted(nums)
        ng = [e for e in sn if e<=0]
        ps = [e for e in sn if e>0]
        ab= sorted([abs(e) for e in sn])
        li=[]
        if sn[0]>0 and k%2==1: return sum(sn[1:])-sn[0]*(1 if k%2 else -1) 
        if  sn[0]<=0 and len(ng)<k : return -sum(ng)-2*ab[0]*(1 if (k-len(ng))%2 else 0)+sum(ps)
        if  sn[0]<=0 and len(ng)>=k : return -sum(ng[:k])+sum(ng[k:])+sum(ps)#-2*ab[0]*(1 if (k-len(ng))%2 else -1)
        #if  len(ng)<k and k-len(ng)%2==0: return sum(ng[:-1])+ng[-1]+sum(ps)
            