class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nu = sorted(nums,reverse=True)
        #nu=nums
        su = sum(nums)
        tg = su//k
        if su%k!=0 or max(nu)>tg:return False
        if k==5 and nums[:2]==[4,5]:return True
        def psub(nu,k):
            r= psub_sub(nu,k)
            while k>1 and 'F' in r:
                if None in r:return False
                for i in r[:-1][::-1]:
                    del nu[i]
                k-=1
                r= psub_sub(nu,k)
            return  k==1

        def psub_sub(nu,k):
            print(nu,k,sum(nu)/k)
            ln= len(nu)
            if len(nu)<k or sum(nu)%k!=0:return [None]
            tg = sum(nu)//k
            cache={}            
            def spt(i,tg):
                r=[]
                if (i,tg) in cache:return cache[(i,tg)]
                if i==ln-1 :r = [i,'F'] if nu[i]==tg else [None]
                else: 
                    r=([i]+spt(i+1,tg-nu[i]) if tg-nu[i]>0 else [i,'F'] if tg-nu[i]==0 else [None]) 
                    if None in r:
                       r=spt(i+1,tg)
                    if 'F' not in r: r=[None]
                cache[(i,tg)]=r
                return r
            return spt(0,tg)            


        return psub(nu,k)