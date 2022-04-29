class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        #  int pre = 0, maxAns = nums[0];
        # for (int x : nums) {
        #     pre = Math.max(pre + x, x);
        #     maxAns = Math.max(maxAns, pre);
        # }
        # return maxAns;
        # }
        def maxsubseq_v3(nums):
            pre,maxans =0,nums[0]
            for n in nums:
                pre = max(pre+n,n)
                maxans=max(maxans,pre)
            return maxans

        def maxsubseq_v2(nums):
            for i in range(1,len(nums)):
                nums[i]=max(nums[i],nums[i]+nums[i-1])
            return max(nums)

        def maxsubseq_v1(nums):
            c, cdiffmax,cleftmin=nums[0],nums[0],nums[0] if nums[0]<0 else 0
            for n in nums[1:]:
                c,cdiffmax,cleftmin, = c+n,max(cdiffmax,c+n-cleftmin),min(c+n,cleftmin)
            return cdiffmax    

        def maxsubseq_v0(nums):
            if not nums:return 0
            n_li=[[0,nums[0],nums[0],nums[0]]]
            for ii in range(1,len(nums)):
                if n_li[-1][-1]<=0:
                    if nums[ii]>n_li[-1][-1]:
                        cmax = nums[ii]
                        cum = nums[ii] 
                    else:
                        cmax = n_li[-1][-1]
                        cum = nums[ii]
                else:
                    if nums[ii]>0:
                        cum = n_li[-1][-1]+nums[ii]
                        cmax =cum
                    elif nums[ii]+n_li[-1][-1]>=0:
                        cmax = n_li[-1][-1]
                        cum = n_li[-1][-1]+nums[ii]
                    elif nums[ii]+n_li[-1][-1]<0:
                        cmax = n_li[-1][-1]
                        cum = nums[ii]                   
                n_li.append([ii,nums[ii],cmax,cum])
            return max([el[2] for el in n_li])

        return maxsubseq_v3(nums)