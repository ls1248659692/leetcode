class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tn=[target-n for n in nums][::-1]
        #while tn and nums and tn[0]!=nums[0]:
        #    v_ = tn.pop(0) if tn[0]<nums[0] else nums.pop(0)
        print(tn,nums)
        i,j=0,0
        while i<len(nums):
            #print(tn[i],nums[j])
            if tn[i]==nums[j]:return [tn[i],target-tn[i]]
            elif tn[i]<nums[j]:i+=1
            else: j+=1
        return  []