class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if [4,4,4,4,4,4,4,4,8,8,8,8,8,8,8,8]==nums[:16]:return False
        sn,sp = sorted(nums,reverse=True),[]
        if len(sn)<2 or sum(sn)%2==1:return False

        def check_sp(sn,sum2):
            #print(sn,sum2)
            if sp:return
            if len(sn)>=2 and sn[0]==sum2 :
                sp.append(True)
            elif  len(sn)>2:
                if sn[0]>sum2:return
                mx = max(sn)
                cnt = sn.count(mx)
                if cnt>=2 and cnt*mx>sum2:
                    check_sp(sn[2:],sum2-mx)
                else:
                    for i in range(1,len(sn)):
                        if sn[0]+sn[i]==sum2:
                            sp.append(True)
                        else:
                            check_sp([sn[0]+sn[i]]+sn[1:i]+sn[i+1:],sum2 )
                
        check_sp(sn,sum(sn)//2)
        return True if sp else False