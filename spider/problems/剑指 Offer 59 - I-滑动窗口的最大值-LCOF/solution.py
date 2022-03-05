class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        list1 = []
        if len(nums) < k:
            return nums
        for i in range(0,len(nums)):
            if len(nums[i:i+k]) == k:
                list1.append(max(nums[i:i+k]))
        return list1

        def calc_mxi(b,e):
            mxli = [e-1]
            for i in range(e-2,b-1,-1):
                if ns[i]>ns[mxli[0]]:
                    mxli.insert(0,i)
            return mxli       
