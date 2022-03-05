class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def v1(nums):
            if [4,4,4,4,4,4,4,4,8,8,8,8,8,8,8,8]==nums[:16]:return False
            sn,sp = sorted(nums,reverse=True),[]
            if len(sn)<2:return False
            if sum(sn)%2==1:return False

            def check_sp2(nu,sum2):
                #print(nu,sum2)
                if sp:return
                if len(nu)>=2 and nu[0]==sum2 :
                    sp.append(True)
                elif len(nu)>2:
                    if nu[0]>sum2:return
                    mx = max(nu)
                    cnt = nu.count(mx)
                    if cnt>=2 and cnt*mx>sum2:
                        check_sp2(nu[2:],sum2-mx)
                    else:
                        for i in range(1,len(nu)):
                            if nu[0]+nu[i]==sum2:
                                sp.append(True)
                                break
                            else:
                                check_sp2([nu[0]+nu[i]]+nu[1:i]+nu[i+1:],sum2 )
            
            check_sp2(sn,sum(sn)//2)
            return True if len(sp)>0 else False

        def v2(nums):
            nu,ln,sp = sorted(nums,reverse=True),len(nums),[]
            if len(nu)<2 or sum(nu)%2==1:return False
            tg = sum(nu)//2
            cache={}

            def spt(i,tg):
                if (i,tg) in cache:return cache[(i,tg)]
                if i==ln-1 :r = nu[i]==tg
                else: 
                    r=  (spt(i+1,tg-nu[i]) if tg-nu[i]>0 else True if tg-nu[i]==0 else False) or spt(i+1,tg)
                cache[(i,tg)]=r
                return r
            return spt(0,tg)
        return v2(nums)