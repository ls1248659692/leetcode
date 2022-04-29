class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ln= len(nums)
        cache={}
        def v1(i,tg):
            if (i,tg) in cache:return cache[(i,tg)]
            if i==ln:
                r= 1 if tg==0 else 0
            else:
                pos = v1(i+1,tg+nums[i]) 
                neg = v1(i+1,tg-nums[i])
                r= pos+neg
            cache[(i,tg)]=r
            return r
        return v1(0,target)