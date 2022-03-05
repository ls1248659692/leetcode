class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True) 
        s=sum(nums) 
        a=0
        l=[]
        for i in range(len(nums)):
            a=a+nums[i]
            l.append(nums[i])
            if a>s-a:
                break
        return l