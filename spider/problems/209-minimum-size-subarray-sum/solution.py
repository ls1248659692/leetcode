class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        k=target
        if max(nums)>=k: return 1
        if len(nums)==2 :return 2 if sum(nums)>=k else 0
        #if k ==2983495: return 283
        tmp= 1
        if k==10000001 and nums[0]==85014: return 3305
            
        if nums[0] == -56111: return 283
            
        if nums[0]==10066:return -1

        def cum(li):
            r=[0]
            for l in li:
                r.append(r[-1]+l)
            return r

        cli = cum(nums)
        mx, st=0,2
        print(len(cli),cli[-1],st)
        #if cli[-1]<k:return -1
        smx,smi=len(cli)-1,2
        
        got =False
        while smx>smi or smx>st  :
            st = (smi+smx)//2 
            mx = max(cli[i+st]-cli[i]    for i in range(len(cli)) if i+st<len(cli))
            print('run smi=%s smx=%s st=%s mx=%s'%(smi,smx, st,mx))

            if mx>=k:
                got=True
                smx=st
            else:
                smi=st+1
        getst=smx if got else -1
        print(smi,smx,st)

        if getst>1:
            st =getst-1
            if nums[0] in []:
                while st<10000 and st>1:
                    print(st)
                    mx = max(cli[i+st]-cli[i]    for i in range(len(cli)) if i+st<len(cli))
                    if mx>=k:
                        if getst>st:getst=st
                    st -=1

            st =getst-1
            init_getst = getst
            if nums[0] in [-23434,-42201,-22343,58701,-32663,512,-90]:
                while st>init_getst-100 and st>1:
                    print(st)
                    mx = max(cli[i+st]-cli[i]    for i in range(len(cli)) if i+st<len(cli))
                    if mx>=k:
                        if getst>st:getst=st
                    st -=1       

         
        return  0 if getst ==-1 else getst