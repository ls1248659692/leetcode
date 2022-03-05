class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def v1(nums):
            if len(nums)<=1:
                return [nums]
            else:
                res = []
                for ii in range(len(nums)):
                    tli = [ [nums[ii]] + el for el in self.permute(nums[:ii]+nums[ii+1:])]
                    res.extend(tli)
                return res

        def v2(nums):   
            def backtrack(first = 0):
                if first == n:  
                    res.append(nums[:])
                for i in range(first, n):
                    nums[first], nums[i] = nums[i], nums[first]
                    backtrack(first + 1)
                    nums[first], nums[i] = nums[i], nums[first] # æ¤éæä½
            
            n = len(nums)
            res = []
            backtrack()
            return res
        return v1(nums)
