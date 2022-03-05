class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        list1 = []
        if len(nums) < k:
            return nums
        for i in range(0,len(nums)-k+1):
            sn = sorted(nums[i:i+k])
            list1.append(sn[k//2] if k%2 else (sn[k//2-1]+sn[k//2])/2)
        return list1

        def calc_mxi(b,e):
            mxli = [e-1]
            for i in range(e-2,b-1,-1):
                if ns[i]>ns[mxli[0]]:
                    mxli.insert(0,i)
            return mxli       

        ns=nums
        if k==1:return ns

        mxli = calc_mxi(0,k)    
        res=[mxli[0]]
        print(res,len(mxli),mxli)
        print(len(nums),k)        