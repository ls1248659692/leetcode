class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dn = {}
        for n in nums:
            dn.setdefault(n,0)
            dn[n]+=1
        st=[(n,dn[n]+dn.get(n+1,-99999)) for n in dn]
        srt = sorted(st,key=lambda xx:xx[1],reverse=True)
        #print(srt)
        return srt[0][1] if srt[0][1]>0 else 0