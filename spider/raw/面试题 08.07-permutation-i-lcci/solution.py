class Solution:
    def permutation(self, S: str) -> List[str]:
        def v1(nums):
            if len(nums)<=1:
                return [nums]
            else:
                res = []
                for ii in range(len(nums)):
                    tli = [ nums[ii] + el for el in v1(nums[:ii]+nums[ii+1:])]
                    res.extend(tli)
                return res
        return v1(S)